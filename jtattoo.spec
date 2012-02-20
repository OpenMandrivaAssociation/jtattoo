# This spec is based on Toni Graffy's from OpenSUSE and
# Alberto Altieri's from MIB work

%define		oname	JTattoo

Name:		jtattoo
# note: to get version call
# java -jar JTattoo.jar com.jtattoo.plaf.About
Version:	1.3
Release:	%mkrel 1
Summary:	JTattoo Look and Feel
License:	see License.html
Group:		Development/Java
Url:		http://www.jtattoo.net/index.html
Source0:	http://www.jtattoo.net/downloads/JTattooSource.zip
Source1:	jtattoo.css
Source2:	JTattooLogo.gif
Source3:	License.html
Requires:	java >= 1.6
BuildRequires:	ant
BuildRequires:	java-devel-openjdk
BuildRequires:	update-alternatives
BuildRequires:	unzip
BuildRequires:	xerces-j2
BuildRequires:	xmlbeans
BuildRequires:	xml-commons-apis
BuildArch:	noarch
%rename		%{oname}

%description
JTattoo consists of several different Look and Feels for Swing
applications. All of them enables developers to improve their
application with an excellent user interface. So JTattoo opens
desktop applications the door to end users who are unfortunate
with the Look and Feels shipped with the standard JDK.

%prep
%setup -q -c -n %{oname}
%__install -m 644 %{SOURCE1} .
%__install -m 644 %{SOURCE2} .
%__install -m 644 %{SOURCE3} .

%build
ant -buildfile build/build.xml jar

%install
%__rm -rf %{buildroot}
export NO_BRP_CHECK_BYTECODE_VERSION=true

# jar
%__install -dm 755 %{buildroot}%{_javadir}
%__install -m 644 build/dist/%{oname}.jar \
	%{buildroot}%{_javadir}/%{oname}-%{version}.jar
pushd %{buildroot}%{_javadir}
	for jar in *-%{version}*; do
		ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`
	done
popd

%clean
%__rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc jtattoo.css JTattooLogo.gif License.html
%{_javadir}/*

