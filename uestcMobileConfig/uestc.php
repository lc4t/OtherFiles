<?php
//print_r ($_POST);
$username = $_POST['username'];
$password = $_POST['password'];

if (strlen($username) >=8 && strlen($password) >= 6)
{
    print (123);
    $data1 = <<<XML1
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>PayloadContent</key>
	<array>
		<dict>
			<key>AutoJoin</key>
			<true/>
			<key>EAPClientConfiguration</key>
			<dict>
				<key>AcceptEAPTypes</key>
				<array>
					<integer>25</integer>
				</array>
				<key>EAPFASTProvisionPAC</key>
				<false/>
				<key>EAPFASTProvisionPACAnonymously</key>
				<false/>
				<key>EAPFASTUsePAC</key>
				<false/>
				<key>UserName</key>
				<string>
XML1;
    $data2 = <<<XML2
</string>
				<key>UserPassword</key>
				<string>
XML2;
    $data3 = <<<XML3
</string>
			</dict>
			<key>EncryptionType</key>
			<string>WEP</string>
			<key>HIDDEN_NETWORK</key>
			<false/>
			<key>PayloadDescription</key>
			<string>Configures wireless connectivity settings.</string>
			<key>PayloadDisplayName</key>
			<string>uestc</string>
			<key>PayloadIdentifier</key>
			<string>com.company.uestc.wifi1</string>
			<key>PayloadOrganization</key>
			<string></string>
			<key>PayloadType</key>
			<string>com.apple.wifi.managed</string>
			<key>PayloadUUID</key>
			<string>C9DEDB2D-A061-4E9B-BC8F-B54CF678911E</string>
			<key>PayloadVersion</key>
			<integer>1</integer>
			<key>ProxyType</key>
			<string>None</string>
			<key>SSID_STR</key>
			<string>uestc</string>
		</dict>
	</array>
	<key>PayloadDescription</key>
	<string>Profile description.</string>
	<key>PayloadDisplayName</key>
	<string>uestc</string>
	<key>PayloadIdentifier</key>
	<string>com.company.uestc</string>
	<key>PayloadOrganization</key>
	<string></string>
	<key>PayloadRemovalDisallowed</key>
	<false/>
	<key>PayloadType</key>
	<string>Configuration</string>
	<key>PayloadUUID</key>
	<string>D4DF97B4-4545-4090-80C4-E6D95D8C60B6</string>
	<key>PayloadVersion</key>
	<integer>1</integer>
</dict>
</plist>
XML3;




    $filename = md5(time() + md5(time()) + md5(rand(0,77e77)));

    mkdir($filename);
    $file = fopen($filename . "/uestc.mobileconfig", "wr+") or die('fail');

    fwrite($file, $data1 . $username . $data2 . $password . $data3);

    fclose($file);
    header("Location: " . $filename . "/uestc.mobileconfig");

};
?>

