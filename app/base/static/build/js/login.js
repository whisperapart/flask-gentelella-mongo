/*
global
alertify: false
*/

/**
 * Create a new account.
 */
function signup() { // eslint-disable-line no-unused-vars
  if ($('#create-user-form').parsley().validate()) {
    $.ajax({
      type: 'POST',
      url: '/create_user',
      dataType: 'json',
      data: $('#create-user-form').serialize(),
      success: function(result) {
        if (result == 'duplicate') {
          const message = '创建失败：已存在。';
          alertify.notify(message, 'error', 5);
        } else {
          alertify.notify('New user created.', 'success', 5);
          document.getElementById('login-button').click();
        }
      },
    });
  }
}
