 1. used the Meta class to create permissions such as can_view, can_create, can_edit, and can_delete
 2. used the admin site to great group and assign permissions
 3. enforced permissions in views
 4. register views to url


 permissions are created in the model.py file and the the assigned to users and groups in view.py file
 they are the link to urls






 specific security settings implemented
1. Set DEBUG to False in production.
2. Configure SECURE_BROWSER_XSS_FILTER, X_FRAME_OPTIONS, and SECURE_CONTENT_TYPE_NOSNIFF to add additional browser-side protections.
3. Ensure CSRF_COOKIE_SECURE and SESSION_COOKIE_SECURE are set to True to enforce that cookies are sent over HTTPS only.
4. Protect Views with CSRF Tokens
5. Secure Data Access in Views
6. Implement Content Security Policy (CSP)