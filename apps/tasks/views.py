from django.core.exceptions import PermissionDenied, ValidationError
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required

from apps.users.mixins import MinisterOrMemberRequiredMixin, MinisterRequiredMixin
from apps.events.models import EventsToOrganize

from apps.tasks.models import Tasks
from apps.users.models import CustomUser

from apps.ministries.forms import MinisterTaskForm
from django.contrib import messages

from apps.events.models import Events


class EventsListView(View):
    def get(self, request):
        events = EventsToOrganize.objects.all()
        return render(request, "events/events_list_internal.html", {"events": events})


class EventDetailView(MinisterOrMemberRequiredMixin,View):
    """Главная страница мероприятия — показывает инфо + задачи + форму создания."""

    def get_context(self, request, event):
        tasks = Tasks.objects.select_related("assigned_to", "ministry").filter(event=event)

        # Для модального окна создания задачи (только министру)
        ministry_members = []
        user_ministries = []
        if request.user.is_authenticated and hasattr(request.user, 'ministry') and request.user.ministry:
            ministry_members = CustomUser.objects.filter(ministry=request.user.ministry)
            user_ministries = [request.user.ministry]  # или Ministry.objects.all() если нужно все

        return {
            "event": event,
            "tasks": tasks,
            "ministry_members": ministry_members,
            "user_ministries": user_ministries,
        }

    def get(self, request, event_id):
        event = get_object_or_404(EventsToOrganize, id=event_id)
        return render(request, "events/event_detail.html", self.get_context(request, event))

    def post(self, request, event_id):
            if not request.user.is_minister:
                raise PermissionDenied
            if request.user.ministry is None:
                raise PermissionDenied("Министр должен быть закреплён за министерством.")

            event = get_object_or_404(EventsToOrganize, id=event_id)
            form = MinisterTaskForm(request.POST)
            form.fields["assigned_to"].queryset = form.fields["assigned_to"].queryset.filter(
                ministry=request.user.ministry
            )
            if form.is_valid():
                task = form.save(commit=False)
                task.ministry = request.user.ministry
                task.save()
                return redirect("event_to_organize_detail", event_id=event_id)

            # если форма невалидна — перерендериваем страницу с ошибками
            return render(request, "events/event_detail.html", {
                **self.get_context(request, event),
                "form_errors": form.errors,  # передаём ошибки в шаблон
            })



class TaskEditView(MinisterRequiredMixin, View):
    def get_task(self, request, task_id):
        task = get_object_or_404(Tasks, id=task_id)
        if task.ministry_id != request.user.ministry_id:
            raise PermissionDenied("Нельзя редактировать задачи другого министерства.")
        return task

    def post(self, request, task_id):
        task = self.get_task(request, task_id)
        task.name = request.POST.get("name", task.name)
        task.description = request.POST.get("description", task.description)
        task.deadline = request.POST.get("deadline", task.deadline)
        task.assigned_to_id = request.POST.get("assigned_to", task.assigned_to_id)
        task.save()
        if task.event_id:
            return redirect("event_to_organize_detail", event_id=task.event_id)
        return redirect("events_list")


class TaskStatusUpdateView(MinisterOrMemberRequiredMixin, View):
    def post(self, request, task_id):
        task = get_object_or_404(Tasks, id=task_id)
        if task.ministry_id != request.user.ministry_id:
            raise PermissionDenied("Можно менять статус только задач своего министерства.")
        new_status = request.POST.get("status")
        if new_status in ("todo", "in_progress", "done"):
            task.status = new_status
            task.save()
        return redirect("event_to_organize_detail", event_id=task.event_id)
    

@method_decorator(staff_member_required,name='dispatch')
class EventDoneView(View):
    def post(self, request,event_organized_id):
        event_organized = get_object_or_404(EventsToOrganize,id=event_organized_id)
        if not event_organized.image:
            messages.error(request,'Вставь картинку к мероприятию')
            return redirect('event_detail_public',event_organized_id=event_organized_id)
        new_public_event = Events.objects.create(
            name=event_organized.name,
            description=event_organized.description,
            date=event_organized.date,
            image=event_organized.image
        )
        return redirect('event_detail_public',event_id=new_public_event.id)
