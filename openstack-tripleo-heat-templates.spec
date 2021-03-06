%global commit0 0f2bf59910639c62442aa3a1266ea4e67d76d25a
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global service tripleo-heat-templates

%{!?upstream_version: %global upstream_version %{version}}

Name:		openstack-tripleo-heat-templates
Summary:	Heat templates for TripleO
Version:    0.8.7
Release:    5%{?dist}
License:	ASL 2.0
Group:		System Environment/Base
URL:		https://wiki.openstack.org/wiki/TripleO
# Once we have stable branches and stable releases we can go back to using release tarballs
Source0:  https://tarballs.openstack.org/%{service}/%{service}-%{version}.tar.gz

#patches_base=+1
Patch0001: 0001-Enable-Dell-Storage-Center-iscsi-Backends-in-Cinder.patch
Patch0002: 0002-Enable-Equallogic-Backends-in-Cinder.patch
Patch0003: 0003-Add-update-yaml-backward-compatibe-with-PublicVirtua.patch
Patch0004: 0004-Align-template-defaults-with-the-client.patch
Patch0005: 0005-Fix-nova.conf-and-neutron.conf-to-support-Nova-Neutr.patch
Patch0006: 0006-Let-Puppet-update-all-packages-on-non-controllers.patch
Patch0007: 0007-neutron-enable-nova-event-callback-by-default.patch
Patch0008: 0008-Add-update-environment-directory-and-sample-file.patch
Patch0009: 0009-Downstream-only-fix-for-VIP-upgrades-from-7.1.patch
Patch0010: 0010-Enable-pacemaker-by-default-for-RDO-Manager.patch
Patch0011: 0011-Enable-PrePuppet-and-PostPuppet-by-default.patch
Patch0012: 0012-rhbz-1235748-Keystone-domain-for-Heat.patch
Patch0013: 0013-Use-KeystoneAdminApiVirtualIP-for-heat-keystone-doma.patch

BuildArch:	noarch
BuildRequires:  git
BuildRequires:	python2-devel
BuildRequires:	python-setuptools
BuildRequires:	python-d2to1
BuildRequires:	python-pbr

Requires:	PyYAML


%description
OpenStack TripleO Heat Templates is a collection of templates and tools for
building Heat Templates to do deployments of OpenStack.

%prep
%autosetup -n %{service}-%{version} -S git
%patch0001 -p1
%patch0002 -p1
%patch0003 -p1
%patch0004 -p1
%patch0005 -p1
%patch0006 -p1
%patch0007 -p1
%patch0008 -p1
%patch0009 -p1
%patch0010 -p1
%patch0011 -p1
%patch0012 -p1
%patch0013 -p1


%build
%{__python2} setup.py build

%install
%{__python2} setup.py install -O1 --skip-build --root=%{buildroot}
install -d -m 755 %{buildroot}/%{_datadir}/%{name}
cp -ar *.yaml %{buildroot}/%{_datadir}/%{name}
cp -ar puppet %{buildroot}/%{_datadir}/%{name}
cp -ar docker %{buildroot}/%{_datadir}/%{name}
cp -ar firstboot %{buildroot}/%{_datadir}/%{name}
cp -ar extraconfig %{buildroot}/%{_datadir}/%{name}
cp -ar environments %{buildroot}/%{_datadir}/%{name}
cp -ar network %{buildroot}/%{_datadir}/%{name}
if [ -d validation-scripts ]; then
  cp -ar validation-scripts %{buildroot}/%{_datadir}/%{name}
fi
if [ -d examples ]; then
  rm -rf examples
fi

%files
%doc README*
%license LICENSE
%{python2_sitelib}/tripleo_heat_merge
%{python2_sitelib}/tripleo_heat_templates-*.egg-info
%{_datadir}/%{name}
%{_bindir}/tripleo-heat-merge

%changelog
* Fri Jan 22 2016 marios <marios@redhat.com> 0.8.7-5
- Use KeystoneAdminApiVirtualIP for heat keystone domain admin setup
- rhbz#1235748 : Keystone domain for Heat
- Enable PrePuppet and PostPuppet by default
- Enable pacemaker by default for RDO Manager
- Downstream only fix for VIP upgrades from 7.1
- Add update environment directory and sample file
- neutron: enable nova-event-callback by default
- Let Puppet update all packages on non-controllers
- Fix nova.conf and neutron.conf to support Nova/Neutron notifications
- Align template defaults with the client
- Add update yaml backward compatibe with PublicVirtualIP on ctlplane
- Enable Equallogic Backends in Cinder
- Enable Dell Storage Center iscsi Backends in Cinder

* Fri Jan 22 2016 marios <marios@redhat.com> 0.8.7-4
- Update to 0.8.7

* Thu Jan 21 2016 Lon Hohberger <lon@redhat.com> 0.8.7-3
- Move patches around

* Thu Nov 19 2015 Mike Burns <mburns@redhat.com> 0.8.7-2
- Enable Equallogic Backends in Cinder
- Enable Dell Storage Center iscsi Backends in Cinder

* Mon Oct 19 2015 John Trowbridge <trown@redhat.com> - 0.8.7-1
- Use a source tarball for a git hash that has passed delorean CI for liberty release

* Mon Oct 20 2014 James Slagle <jslagle@redhat.com> 0.7.9-5
- Update patches

* Mon Oct 20 2014 James Slagle <jslagle@redhat.com> 0.7.9-4
- Update patches

* Wed Oct 15 2014 James Slagle <jslagle@redhat.com> 0.7.9-3
- Adding SNMP related parameters to storage templates
- Add converted version of block and object storage
- Compute and controller templates without merge.py

* Wed Oct 15 2014 James Slagle <jslagle@redhat.com> 0.7.9-2


* Wed Oct 15 2014 James Slagle <jslagle@redhat.com> 0.7.9-1
- Update to upstream 0.7.9

* Tue Oct 07 2014 James Slagle <jslagle@redhat.com> 0.7.7-3
- Adding SNMP related parameters to storage templates

* Mon Oct 06 2014 James Slagle <jslagle@redhat.com> 0.7.7-2
- Add converted version of block and object storage
- Compute and controller templates without merge.py

* Mon Sep 29 2014 James Slagle <jslagle@redhat.com> 0.7.7-1
- Update to upstream 0.7.7

* Mon Sep 15 2014 James Slagle <jslagle@redhat.com> 0.7.6-1
- Update to upstream 0.7.6

* Thu Jun 26 2014 James Slagle <jslagle@redhat.com> - 0.4.4-3
- Remove patch that swiched to qpid, we are back to rabbit

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 14 2014 James Slagle <jslagle@redhat.com> - 0.4.4-1
- Bump to 0.4.4 and update patches

* Thu Apr 10 2014 James Slagle <jslagle@redhat.com> - 0.4.2-5
- Add patch to use IP address for MySQL connection

* Thu Mar 27 2014 James Slagle <jslagle@redhat.com> - 0.4.2-4
- Update patch 0001-Add-BlockStorageConfig0.patch to include NeutronNetworkType
  parameter.

* Wed Mar 26 2014 James Slagle <jslagle@redhat.com> - 0.4.2-3
- Update patches

* Tue Mar 25 2014 James Slagle <jslagle@redhat.com> - 0.4.2-2
- Add patch 0003-Expose-dnsmasq-options.patch

* Mon Mar 24 2014 James Slagle <jslagle@redhat.com> - 0.4.2-1
- Bump to 0.4.2.

* Fri Mar 21 2014 James Slagle <jslagle@redhat.com> - 0.4.1-1
- Rebase onto 0.4.1.
- Add patch to switch from rabbit to qpid as default message bus

* Wed Mar 12 2014 James Slagle <jslagle@redhat.com> - 0.4.0-2
- Remove python BuildRequires
- Switch __python to __python2 macro
- Switch python_sitelib to python2_sitelib macro
- Use doc macro for README.md, LICENSE, and examples
- Use name macro when copying templates in install

* Mon Feb 17 2014 James Slagle <jslagle@redhat.com> - 0.4.0-1
- Update spec file for Fedora Packaging

* Thu Sep 19 2013 Ben Nemec <bnemec@redhat.com> - 0.0.1-1
- First build of tripleo-heat-templates
