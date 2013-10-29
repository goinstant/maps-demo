window.goinstant = window.goinstant || {};
window.goinstant.SendInvite = (function() {

/*jshint browser:true, node:false*/

"use strict";

/**
 *
 */
var $ = window.$;
var _ = window._;

/**
 * @constructor
 */
function SendInvite() {
  this._$inviteModal = $('#invite_modal');

  _.bindAll(this, '_invite');
}

SendInvite.prototype.initialize = function() {
  var self = this;

  var $inviteModalBody = $('#invite_modal_body');

  $inviteModalBody.on('keypress', '.invite_phone', function(e) {
    if(e.which == 13) {
      self._invite();
    }
  });

  $inviteModalBody.on('keypress', '.invite_email', function(e) {
    if(e.which == 13)  {
      self._invite();
    }
  });

  $inviteModalBody.on('keyup', '.invite_phone', function() {
    $(this).parent().parent().removeClass('success');
    $(this).parent().parent().removeClass('error');
  });

  $inviteModalBody.on('keyup', '.invite_email', function() {
    $(this).parent().parent().removeClass('success');
    $(this).parent().parent().removeClass('error');
  });

  $('#invite_form_submit').click(this._invite);

  $('#sms_visible').addClass('btn-primary');
  $('#invite_email_contain').addClass('hidden_field');

  $('#invite_toggle button').click(function() {
    if (!$(this).hasClass('btn-primary')) {
      $('#invite_toggle button').toggleClass('btn-primary');
      $('#invite_phone_contain').toggleClass('hidden_field');
      $('#invite_email_contain').toggleClass('hidden_field');
    }
  });
};

/**
 * Invite
 * @private
 */
SendInvite.prototype._invite = function() {
  this._inviteEmail();
  this._invitePhone();
  //this._$inviteModal.modal('toggle');
};

/**
 * Invite Phone
 * @private
 */
SendInvite.prototype._invitePhone = function() {
  var self = this;

  var phoneField = $('.invite_phone');
  var statusDiv = phoneField.parent().parent();
  if (!(statusDiv.hasClass('success') || statusDiv.hasClass('error'))) {
    if (phoneField.val() !== '') {
      $.ajax({
        url: '/invite/sms',
        type: 'post',
        data: {number: phoneField.val()},
        timeout: 3000,
        success: function () {
          self._$inviteModal.modal('hide');
          phoneField.val('');
        },
        error: function () {
          statusDiv.removeClass('success');
          statusDiv.addClass('error');
          self._$inviteModal.modal('show');
        }
      });
    }
  }
};

/**
 * Invite Email
 * @private
 */
SendInvite.prototype._inviteEmail = function() {
  var self = this;

  var emailField = $('.invite_email');
  var statusDiv = emailField.parent().parent();
  if (!(statusDiv.hasClass('success') || statusDiv.hasClass('error'))) {
    if (emailField.val() !== '') {
      $.post('/invite/email', { email: emailField.val() })
      .success(function () {
        self._$inviteModal.modal('hide');
        emailField.val('');
      })
      .fail(function () {
        statusDiv.removeClass('success');
        statusDiv.addClass('error');
        self._$inviteModal.modal('show');
      });
    }
  }
};

return SendInvite;

})();
