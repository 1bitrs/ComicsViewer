$(window).load(function() {
	imagesize();
	$("#all").click(function() {
		imagesize();
		$('#zoom').val(100);
		$('#zoom').disabled = false;
		display_zoom();
	});
	$("#original").click(function() {
		$('#thumbnail').removeAttr('width');
		$('#thumbnail').removeAttr('height');
		$('#zoom').val(100);
		$('#zoom').disabled = true;
		display_original();
	});
	$(window).keydown(function(e) {
		switch (e.keyCode) {
		case 65:
		case 37:
			event.returnValue = false;
			var url = $('#thumbnail').attr('src');
			var match = url.match(/(http.+\/)(\d{1,3})\.(jpg|jpeg|gif|png)/i);
			var num = parseInt(match[2].replace(/^0+/, ''));
			if (num > 1) {
				document.getElementById("page_number").selectedIndex = num - 2;
				$('#page_number').trigger('change');
			}
			break;
		case 87:
		case 38:
			event.returnValue = false;
			$("input[name='view']").val(["all"]);
			$('#zoom').disabled = false;
			var index = document.getElementById("zoom").selectedIndex;
			if (index - 1 >= 0) {
				document.getElementById("zoom").selectedIndex = index - 1;
				$('#zoom').trigger('change');
			}
			break;
		case 68:
		case 39:
			event.returnValue = false;
			$('#wrap a').trigger('click');
			break;
		case 83:
		case 40:
			event.returnValue = false;
			$("input[name='view']").val(["all"]);
			$('#zoom').disabled = false;
			var index = document.getElementById("zoom").selectedIndex;
			if (index + 1 <= 10) {
				document.getElementById("zoom").selectedIndex = index + 1;
				$('#zoom').trigger('change');
			}
			break;
		}
	});
});

function imagesize() {
	$('#thumbnail').removeAttr('width');
	$('#thumbnail').removeAttr('height');
	var img_width = $('#thumbnail').width();
	var img_height = $('#thumbnail').height();
	var window_width = $(window).width();
	var window_height = $(window).height() - 100;
	var ratio_width = img_width / window_width;
	var ratio_height = img_height / window_height;
	if (ratio_width > 1 || ratio_height > 1) {
		if (ratio_width > ratio_height) {
			$('#thumbnail').attr('width', window_width);
		} else {
			$('#thumbnail').attr('height', window_height);
		}
	}
	display_zoom();
}

function Selc(Obj) {
	var file = $('#page_number option:selected').attr('file');
	$('#thumbnail').attr('src', file);
}

function zm(Obj) {
	var index = Obj.selectedIndex;
	imagesize();
	var magnification = $('#thumbnail').width() * Obj.options[index].value / 100;
	$('#thumbnail').attr('width', magnification);
	$('#thumbnail').removeAttr('height');
	display_zoom();
}

function chgImg(maxcount) {
	index = document.getElementById("page_number").selectedIndex;
	if( (index+1) >= maxcount)
		index = -1
	document.getElementById("page_number").selectedIndex = index + 1;
	$('#thumbnail').attr('src', imgData[index + 1]);
	$('#thumbnail2').attr('src', imgData[index + 2]);
	scrollTo(0,0);
}

function display_zoom() {
	$('#contents').css({
		'width': '56%'
	});
	$('#iad_left').css({
		'display': 'block'
	});
	$('#ads_right').css({
		'display': 'block'
	});
}

function display_original() {
	$('#contents').css({
		'width': '100%'
	});
	$('#iad_left').css({
		'display': 'none'
	});
	$('#ads_right').css({
		'display': 'none'
	});
}