# fix php file name with regex
exec { 'fix file name':
  command => 'sed -i s/phpp/php/g var/www/html/wp-settings.php',
  provider=>shell,
}
