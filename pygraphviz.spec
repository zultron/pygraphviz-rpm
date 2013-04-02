Name:           pygraphviz
Version:        1.1
Release:        0%{?dist}
Summary:        A Python interface to Graphviz
Group:          Development/Languages

License:        BSD
URL:            http://networkx.lanl.gov/pygraphviz
Source0:        https://pypi.python.org/packages/source/p/pygraphviz/%{name}-%{version}.tar.gz

BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  graphviz-devel
BuildRequires:  python-sphinx


%description

PyGraphviz is a Python interface to the Graphviz graph layout and
visualization package. With PyGraphviz you can create, edit, read,
write, and draw graphs using Python to access the Graphviz graph data
structure and layout algorithms. PyGraphviz is independent from
NetworkX but provides a similar programming interface.

%prep
%setup -q
#%%setup -q -n %{name}-%{version}


%build
%{__python} setup.py build

# build the docs

# pygraphviz is needed to build the docs
export PYTHONPATH="`echo $(pwd)/build/lib.linux-*`"

pushd doc
make html
rm build/html/.buildinfo
popd


%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

 
%check
%{__python} setup_egg.py nosetests

%files
%doc README.txt examples doc/build/html
%{python_sitearch}/*


%changelog
* Mon Apr  1 2013 John Morris <john@zultron.com> - 1.1-0
- Initial package

