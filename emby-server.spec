# TODO
# - emby user
%include	/usr/lib/rpm/macros.mono
Summary:	Emby: home media server
Name:		emby-server
Version:	3.0.5607.2
Release:	0.1
License:	GPL
Group:		Applications/Multimedia
Source0:	https://github.com/MediaBrowser/MediaBrowser/archive/%{version}.tar.gz
# Source0-md5:	84f0e9a3ee083622562cae203583a65b
URL:		http://emby.media/
BuildRequires:	mono >= 3.2.7
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	rpmbuild(monoautodeps)
Requires:	ImageMagick >= 6.8
Requires:	libmediainfo
Requires:	mono >= 3.2.7
Requires:	sqlite3 >= 3.8.2
Obsoletes:	MediaBrowserServer
Obsoletes:	MediaBrowserServer-dev
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_prefix}/lib/%{name}

%description
Emby (formely known as Media Browser) is a home media server built on
top of other popular open source technologies such as Service Stack,
jQuery, jQuery mobile, and Mono. It features a REST-based api with
built-in documention to facilitate client development. We also have
client libraries for our API to enable rapid development.

%prep
%setup -qc
mv MediaBrowser-%{version} src
install -d bin

%build
cd src
xbuild /p:Configuration="Release Mono" /p:Platform="Any CPU" /t:clean MediaBrowser.Mono.sln
xbuild /p:Configuration="Release Mono" /p:Platform="Any CPU" /t:build MediaBrowser.Mono.sln

mv MediaBrowser.Server.Mono/bin/Release\ Mono/* ../bin
cd ..

rm -v bin/lib*.dylib
rm -v bin/MediaInfo/osx/lib*.dylib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -a bin/* $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_appdir}
%{_appdir}/BDInfo.dll
%{_appdir}/DvdLib.dll
%{_appdir}/Emby.Drawing.dll
%{_appdir}/Emby.Drawing.dll.mdb
%{_appdir}/ImageMagickSharp.dll
%{_appdir}/ImageMagickSharp.dll.config
%{_appdir}/Interfaces.IO.dll
%{_appdir}/MediaBrowser.Api.dll
%{_appdir}/MediaBrowser.Common.Implementations.dll
%{_appdir}/MediaBrowser.Common.dll
%{_appdir}/MediaBrowser.Controller.dll
%{_appdir}/MediaBrowser.Dlna.dll
%{_appdir}/MediaBrowser.IsoMounting.Linux.dll
%{_appdir}/MediaBrowser.LocalMetadata.dll
%{_appdir}/MediaBrowser.MediaEncoding.dll
%{_appdir}/MediaBrowser.MediaInfo.dll
%{_appdir}/MediaBrowser.MediaInfo.dll.config
%{_appdir}/MediaBrowser.Model.dll
%{_appdir}/MediaBrowser.Model.dll.mdb
%{_appdir}/MediaBrowser.Naming.dll
%{_appdir}/MediaBrowser.Providers.dll
%{_appdir}/MediaBrowser.Server.Implementations.dll
%{_appdir}/MediaBrowser.Server.Mono.exe
%{_appdir}/MediaBrowser.Server.Mono.exe.config
%{_appdir}/MediaBrowser.Server.Startup.Common.dll
%{_appdir}/MediaBrowser.WebDashboard.dll
%{_appdir}/MediaBrowser.XbmcMetadata.dll
%{_appdir}/Mono.Nat.dll
%{_appdir}/Mono.Posix.dll
%{_appdir}/MoreLinq.dll
%{_appdir}/NLog.dll
%{_appdir}/OpenSubtitlesHandler.dll
%{_appdir}/Patterns.Logging.dll
%{_appdir}/ServiceStack.Api.Swagger.dll
%{_appdir}/ServiceStack.Client.dll
%{_appdir}/ServiceStack.Common.dll
%{_appdir}/ServiceStack.Interfaces.dll
%{_appdir}/ServiceStack.Text.dll
%{_appdir}/ServiceStack.dll
%{_appdir}/SharpCompress.dll
%{_appdir}/SimpleInjector.dll
%{_appdir}/SocketHttpListener.dll
%{_appdir}/System.Data.SQLite.dll
%{_appdir}/System.Data.SQLite.dll.config
%{_appdir}/UniversalDetector.dll
%{_appdir}/WebMarkupMin.Core.dll
%{_appdir}/taglib-sharp.dll

%{_appdir}/dashboard-ui
%{_appdir}/swagger-ui
