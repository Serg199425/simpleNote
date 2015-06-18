$(document).ready(function () {
	get_groups()
	setInterval(get_groups, 2000);
	function get_groups() {
		$.ajax({
			url: "/get_groups_invitations/",
			datatype: "json",
			type: "GET",
			success: function (result) {
				add_groups(result.html);
			},
		});
	}

	function add_groups(html) {
		$('.groups-invitations-container').html(html);
	}
});