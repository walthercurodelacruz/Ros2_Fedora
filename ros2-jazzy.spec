%define debug_package %{nil}
%define __brp_check_rpaths %{nil}
%define __brp_mangle_shebangs %{nil}
Name:           ros2-jazzy
Version:        1.0
Release:        2%{?dist}
Summary:        ROS 2 Jazzy Jalisco precompilado para Fedora 44

License:        Apache-2.0
URL:            https://docs.ros.org/en/jazzy/
Source0:        ros2-jazzy-fedora44-x86_64.tar.gz

# Desactivamos el escaneo automático de dependencias para evitar falsos positivos
AutoReqProv:    no

# Dependencias que el usuario debe tener instaladas (GUI, renderizado 3D, logging y runtime)
Requires:       python3-qt5 python3-qt5-devel sip qt5-qtbase-devel urdfdom-headers-devel console-bridge libXaw yaml-cpp tinyxml2 assimp pugixml poly2tri spdlog bullet opencv

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

# Corrige y normaliza los shebangs de Python para usar el intérprete del sistema
find %{buildroot}/opt/ros/jazzy/bin -type f -exec sed -i -E '1s|^#\!.*python3.*|#!/usr/bin/python3|' {} +

%files
# Le decimos al RPM de qué archivos es dueño
/opt/ros/jazzy/

%changelog
* Thu Jul 23 2026 Walther Curo De La Cruz - 1.0-2
- Corrección de dependencias faltantes para RViz2 y librerías dinámicas del sistema (console-bridge, assimp, spdlog, yaml-cpp, etc.)
- Normalización de shebangs de Python hacia /usr/bin/python3 en ejecutables de /opt/ros/jazzy/bin
* Thu Jul 23 2026 Tu Nombre  - 1.0-1
- Empaquetado inicial de binarios nativos para Fedora 44
