from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, required=True, label="Kullanıcı Adı")
    password = forms.CharField(max_length=30, required=True, label="Şifre", widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=30, required=True, label="Kullanıcı Adı")
    password = forms.CharField(max_length=30, required=True, label="Şifre", widget=forms.PasswordInput)
    passwordConfirm = forms.CharField(max_length=30, required=True, label="Şifreyi doğrula", widget=forms.PasswordInput)
    email = forms.EmailField(label="E-mail", required=False)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        passwordConfirm = self.cleaned_data.get("passwordConfirm")
        email = self.cleaned_data.get("email")

        if password and passwordConfirm and password != passwordConfirm:
            raise forms.ValidationError("Şifreler eşleşmiyor!")

        values = {
            "username": username,
            "password": password,
            "email": email
        }

        return values