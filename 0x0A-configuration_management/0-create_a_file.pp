# a file in tmp with ower www-data
file { '/tmp/school':
    ensure  => 'file',
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
    #source  => '/tmp/school',
    content => 'I love Puppet'
}