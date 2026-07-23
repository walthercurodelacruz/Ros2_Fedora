%define debug_package %{nil}
%define __brp_check_rpaths %{nil}
%define __brp_mangle_shebangs %{nil}
Name:           ros2-jazzy
Version:        1.0
Release:        1%{?dist}
Summary:        ROS 2 Jazzy Jalisco precompilado para Fedora 44

License:        Apache-2.0
URL:            https://docs.ros.org/en/jazzy/
Source0:        ros2-jazzy-fedora44-x86_64.tar.gz

# Desactivamos el escaneo automático de dependencias para evitar falsos positivos
AutoReqProv:    no

# Dependencias que el usuario debe tener instaladas (las que descubrimos)
Requires:       python3-qt5 python3-qt5-devel sip qt5-qtbase-devel urdfdom-headers-devel

%description
Binarios precompilados de ROS 2 Jazzy Jalisco. Este paquete instala el framework
robótico directamente en /opt/ros/jazzy, listo para ser utilizado en Fedora 44.

%prep
# Extrae el tar.gz en un directorio temporal de construcción
%setup -q -c -n ros2-jazzy

%install
# Crea el directorio de destino final
mkdir -p %{buildroot}/opt/ros/jazzy
# Copia todo el contenido de tu carpeta 'install' al directorio destino
cp -r install/* %{buildroot}/opt/ros/jazzy/

%files
# Le decimos al RPM de qué archivos es dueño
/opt/ros/jazzy/

%changelog
* Thu Jul 23 2026 Tu Nombre  - 1.0-1
- Empaquetado inicial de binarios nativos para Fedora 44
