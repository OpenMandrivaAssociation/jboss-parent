Name:                 jboss-parent
Version:              55
Release:              1
Group:                Development/Java
Summary:              JBoss Parent POM
License:              Public Domain
URL:                  https://github.com/jboss/jboss-parent-pom
Source0:              https://github.com/jboss/jboss-parent-pom/archive/refs/tags/jboss-parent-%{version}.tar.gz
BuildArch:            noarch
BuildSystem:	maven
BuildOption:	validate

%description
The Project Object Model files for JBoss packages.

%prep
%setup -n jboss-parent-pom-jboss-parent-%{version}

%files -f .mfiles
%doc README.adoc
