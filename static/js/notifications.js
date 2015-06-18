$(document).ready(function () {
	get_notifications()
	setInterval(get_notifications, 2000);
	friends_invitations_count = 0;
	unreaded_notes_count = 0;
	groups_invitations_count = 0;

	function get_notifications() {
		$.ajax({
			url: "/get_notifications/",
			datatype: "json",
			type: "GET",
			success: function (result) {
				change_friends_count(result);
				change_unreaded_notes_count(result);
				change_groups_invitations_count(result);
			},
		});
	}

	function change_friends_count(result) {
		if (friends_invitations_count != result.friends_invitations_count) {
			friends_invitations_count = result.friends_invitations_count;
			$('#friends_count').remove();
			if (result.friends_invitations_count > 0) {
				$('#friends_button').append('<span class="label label-info pull-right" id="friends_count">'
					+ friends_invitations_count + '</span>')
			}
		}
	}

	function change_unreaded_notes_count(result) {
		if (unreaded_notes_count != result.unreaded_notes_count) {
			unreaded_notes_count = result.unreaded_notes_count;
			$('#shared_notes_count').remove();
			if (result.unreaded_notes_count > 0) {
				$('#shared_notes_button').append('<span class="label label-info pull-right" id="shared_notes_count">'
					+ unreaded_notes_count + '</span>')
			}
		}
	}

	function change_groups_invitations_count(result) {
		if (groups_invitations_count != result.groups_invitations_count) {
			groups_invitations_count = result.groups_invitations_count;
			$('#groups_invitations_count').remove();
			if (result.groups_invitations_count > 0) {
				$('#groups_button').append('<span class="label label-info pull-right" id="groups_invitations_count">'
					+ groups_invitations_count + '</span>')
			}
		}
	}
});