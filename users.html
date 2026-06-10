function initAuthPage() {
  const loginForm = document.getElementById('login-form');
  const registerForm = document.getElementById('register-form');
  const forgotForm = document.getElementById('forgot-form');

  // =====================
  // LOGIN
  // =====================
  if (loginForm) {
    loginForm.addEventListener('submit', async (event) => {
      event.preventDefault();

      const email = loginForm.email.value.trim();
      const password = loginForm.password.value.trim();

      const messageBox =
        document.getElementById('auth-message');

      if (!email || !password) {
        messageBox.textContent =
          'Email and password are required.';
        messageBox.className = 'auth-error';
        return;
      }

      try {
        const response = await apiRequest(
          '/auth/login',
          'POST',
          {
            email,
            password
          }
        );

        console.log('Login Response:', response);

        if (response.access_token) {

          localStorage.setItem(
            'sqlMigratorToken',
            response.access_token
          );

          setUserInfo({
            email,
            role: response.role
          });

          messageBox.textContent =
            'Login successful';

          messageBox.className =
            'auth-success';

          setTimeout(() => {

            if (
              response.role &&
              response.role.toLowerCase() ===
                'admin'
            ) {

              window.location.href =
                '../pages/admin_dashboard.html';

            } else {

              window.location.href =
                '../pages/user_dashboard.html';

            }

          }, 1000);

        } else {

          messageBox.textContent =
            response.message ||
            'Login failed';

          messageBox.className =
            'auth-error';
        }

      } catch (error) {

        console.error(error);

        messageBox.textContent =
          error.message ||
          'Login failed';

        messageBox.className =
          'auth-error';
      }
    });
  }

  // =====================
  // REGISTER
  // =====================
  if (registerForm) {

    registerForm.addEventListener(
      'submit',
      async (event) => {

        event.preventDefault();

        const username =
          registerForm.fullname.value.trim();

        const email =
          registerForm.email.value.trim();

        const password =
          registerForm.password.value.trim();

        const confirmPassword =
          registerForm.confirmPassword.value.trim();

        const role =
          registerForm.role.value;

        const messageBox =
          document.getElementById(
            'auth-message'
          );

        if (
          !username ||
          !email ||
          !password
        ) {

          messageBox.textContent =
            'All fields are required.';

          messageBox.className =
            'auth-error';

          return;
        }

        if (
          password !== confirmPassword
        ) {

          messageBox.textContent =
            'Passwords do not match.';

          messageBox.className =
            'auth-error';

          return;
        }

        try {

          const response =
            await apiRequest(
              '/auth/register',
              'POST',
              {
                username,
                email,
                password,
                role
              }
            );

          console.log(
            'Register Response:',
            response
          );

          messageBox.textContent =
            response.message ||
            'Registration successful';

          messageBox.className =
            'auth-success';

          registerForm.reset();

        } catch (error) {

          console.error(error);

          messageBox.textContent =
            error.message ||
            'Registration failed';

          messageBox.className =
            'auth-error';
        }
      }
    );
  }

  // =====================
  // FORGOT PASSWORD
  // =====================
  if (forgotForm) {

    forgotForm.addEventListener(
      'submit',
      async (event) => {

        event.preventDefault();

        const email =
          forgotForm.email.value.trim();

        const messageBox =
          document.getElementById(
            'auth-message'
          );

        if (!email) {

          messageBox.textContent =
            'Email is required.';

          messageBox.className =
            'auth-error';

          return;
        }

        try {

          const response =
            await apiRequest(
              '/auth/forgot-password',
              'POST',
              { email }
            );

          messageBox.textContent =
            response.message ||
            'Password reset link sent';

          messageBox.className =
            'auth-success';

          forgotForm.reset();

        } catch (error) {

          console.error(error);

          messageBox.textContent =
            error.message ||
            'Request failed';

          messageBox.className =
            'auth-error';
        }
      }
    );
  }
}

// Initialize page
document.addEventListener(
  'DOMContentLoaded',
  initAuthPage
);