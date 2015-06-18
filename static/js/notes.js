$(document).ready(function () {
	get_shared_notes()
	setInterval(get_shared_notes, 2000);
	function get_shared_notes() {
		$.ajax({
			url: "/get_shared_notes/",
			datatype: "json",
			type: "GET",
			success: function (result) {
				add_shared_notes(result.html);
			},
		});
	}

	function add_shared_notes(html) {
		$('.shared-notes-container').html(html);
	}
});
