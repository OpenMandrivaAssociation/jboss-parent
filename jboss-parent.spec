Name:                 jboss-parent
Version:              6
Release:              7
Summary:              JBoss Parent POM
Group:                Development/Java
License:              LGPLv2+
URL:                  http://www.jboss.org/

# git clone git://github.com/jboss/jboss-parent-pom.git
# cd jboss-parent-pom/ && git archive --format=tar --prefix=jboss-parent-6/ 6 | xz > jboss-parent-6.tar.xz
Source0:              %{name}-%{version}.tar.xz
# Removing unavailable deps
Patch0:               %{name}-%{version}-deps.patch
BuildArch:            noarch

BuildRequires:        jpackage-utils
BuildRequires:        maven
BuildRequires:        maven-install-plugin
BuildRequires:        maven-javadoc-plugin
BuildRequires:        maven-release-plugin
BuildRequires:        maven-resources-plugin
BuildRequires:        maven-enforcer-plugin


Requires:             jpackage-utils
Requires:             java
Requires:             maven


%description
The Project Object Model files for JBoss packages.

%prep
%setup -q
%patch0 -p1

%build
mvn-rpmbuild install javadoc:aggregate

%install
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.jboss-%{name}.pom

%add_maven_depmap JPP.jboss-%{name}.pom

%files
%doc README.md
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

