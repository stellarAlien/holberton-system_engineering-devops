# fix php file name with regex
exec {
  command => 'sed -i s/phpp/php/g var/www/html/wp-settings.php',
  provider=>shell,
}
