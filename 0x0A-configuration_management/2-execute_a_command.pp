# Puppet Manifest Executes Kills A Process Named killmenow
 the kil command in puppet

exec { 'pkill killmenow':
  path => '/usr/bin',
}
