# a file in tmp with ower www-data
file{'/tmp/school':
    mode  => '0744',
    owner => 'www-data',
    group => 'www-data',
}