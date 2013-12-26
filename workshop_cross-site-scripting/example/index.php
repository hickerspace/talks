<!DOCTYPE html>
<html>
	<body>
		<form method="GET">
			<div style="color:red;" id="error">
				<?php
					if (isset($_GET["benutzername"])) {
						# Eingaben nicht escapen, um das Beispiel einfach zu halten
						$benutzername = get_magic_quotes_gpc() 
							? stripslashes($_GET["benutzername"]) : $_GET["benutzername"];
						echo "Der Benutzer existiert nicht: $benutzername";
					}
				?>
			</div>

			Benutzername: <input type="text" name="benutzername" />
			Passwort: <input type="password" name="passwort" />
			<input type="submit" />
		</form>
	</body>
</html>
