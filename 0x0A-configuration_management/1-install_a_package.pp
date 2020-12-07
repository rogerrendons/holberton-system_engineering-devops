# puppet manifest to install puppet-lint version 2.1.1 package.

package { 'puppet-lint':
  ensure   => '2.1.1',
  provider => 'gem',
}
