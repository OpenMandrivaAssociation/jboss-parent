%{?_javapackages_macros:%_javapackages_macros}
Name:                 jboss-parent
Version:              11
Release:              1.3
Group:                Development/Java
Summary:              JBoss Parent POM
License:              Public Domain
URL:                  http://www.jboss.org/
Source0:              https://github.com/jboss/jboss-parent-pom/archive/86bff326310a192ef657d893fa8e96ebd33e1ae4.tar.gz
BuildArch:            noarch

BuildRequires:        maven-local
BuildRequires:        maven-install-plugin
BuildRequires:        maven-javadoc-plugin
BuildRequires:        maven-release-plugin
BuildRequires:        maven-resources-plugin
BuildRequires:        maven-enforcer-plugin

%description
The Project Object Model files for JBoss packages.

%prep
%setup -n jboss-parent-pom-86bff326310a192ef657d893fa8e96ebd33e1ae4

%pom_remove_plugin ":maven-clover2-plugin"
%pom_remove_plugin ":findbugs-maven-plugin"
%pom_remove_plugin ":sonar-maven-plugin"
%pom_remove_plugin ":javancss-maven-plugin"

%pom_remove_dep com.sun:tools
%pom_add_dep com.sun:tools

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md

%changelog
* Tue Sep 10 2013 Marek Goldmann <mgoldman@redhat.com> - 11-1
- Upstream release 11
- License change

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 6-9
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr 19 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 6-7
- Simplify requires since they are only in depManagement

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 12 2011 Alexander Kurtakov <akurtako@redhat.com> 6-5
- Add missing BR.

* Tue Sep 20 2011 Marek Goldmann <mgoldman@redhat.com> 6-4
- Removed unavailable deps from POM

* Mon Aug 29 2011 Marek Goldmann <mgoldman@redhat.com> 6-3
- Added maven-surefire-provider-junit requires

* Thu Jul 28 2011 Marek Goldmann <mgoldman@redhat.com> 6-2
- Added build section
- Removed unnecessary sections and BR's

* Mon Jul 18 2011 Marek Goldmann <mgoldman@redhat.com> 6-1
- Upstream release: 6.

* Tue Jun 07 2011 Marek Goldmann <mgoldman@redhat.com> 6-0.1.beta2
- Initial packaging
