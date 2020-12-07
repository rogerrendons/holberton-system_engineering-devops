# Puppet Manifest Executes Kills A Process Named killmenow

exec { 'pkill killmenow':
  path => '/usr/bin',
}
