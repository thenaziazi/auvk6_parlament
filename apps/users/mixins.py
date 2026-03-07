from django.contrib.auth.mixins import UserPassesTestMixin

class MinisterRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_minister or self.request.user.is_staff)

class MemberRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_member or self.request.user.is_staff)
    
class MinisterOrMemberRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return (
            self.request.user.is_authenticated and
            (self.request.user.is_minister or self.request.user.is_member or self.request.user.is_staff))
        