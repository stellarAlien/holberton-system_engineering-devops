# puppet script to manage nginx file limit
exec{'fix file limit':
  onlyif  => 'test -e /etc/default/nginx',
  command => 'sed -i "s/15/4096/" /etc/default/nginx && sudo service nginx restart',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  }
