from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **kwargs):
        if not username:
            raise ValueError("Le nom d'utilisateur est obligatoire.")
        username = self.model.normalize_username(username)
        user = self.model(username=username, **kwargs)
        if password:
            user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password=None, **kwargs):
        kwargs["is_staff"] = True
        kwargs["is_superuser"] = True
        kwargs["is_active"] = True
        return self.create_user(username=username, password=password, **kwargs)
