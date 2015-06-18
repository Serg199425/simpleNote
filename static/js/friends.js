$(document).ready(function () {
	get_friends()
	setInterval(get_friends, 2000);
	function get_friends() {
		$.ajax({
			url: "/get_friends/",
			datatype: "json",
			type: "GET",
			success: function (result) {
				add_friends(result.html);
			},
		});
	}

	function add_friends(html) {
		$('.friends-container').html(html);
	}
});