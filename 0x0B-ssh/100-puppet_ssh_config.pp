#using Puppet to make changes to config file
file_line { 'no passwd auth':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => "PasswordAuthentication no",
  match  => 'PasswordAuthentication yes',
}

file_line { 'identity file':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => "IdentityFile ~/.ssh/school",
  match  => 'IdentityFile ~/.ssh/school',
}