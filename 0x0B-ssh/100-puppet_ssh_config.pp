#!/usr/bin/env bash
# make change to config file using puppet

file {'/etc/ssh/ssh_config':
	ensure => 'present',
}
file_line {'Turn off passed auth':
}
	path 	=> '/etc/ssh/ssh_config',
	line 	=> 'PasswordAuthentication no',
	match	=> 'PasswordAuthentication yes',
	replace => 'true',
file_line {'use a Identity file':
        path    => '/etc/ssh/ssh_config',
        line    => 'IdenfityFile ~/.ssh/config',
        match   => '^Identityfile',
        ensure	=> 'present',
}
