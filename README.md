# Noticias UNA CIAP Calabozo
Noticias UNA CIAP Calabozo es un proyecto comunitario creado por y para estudiantes, profesores y personal de la Universidad Nacional Abierta (UNA), UNA CIAP Calabozo. Surge como una iniciativa para fortalecer la comunicación interna y fomentar la participación activa de los miembros de la comunidad universitaria.

Nuestra plataforma digital tiene como objetivo centralizado servir como fuente de información confiable y actualizada sobre noticias, eventos académicos y novedades relevantes para la comunidad universitaria. A través de Noticias UNA CIAP Calabozo, los usuarios pueden acceder a:

- Noticias de última hora sobre el acontecer diario de la universidad.
- Información detallada sobre las actividades académicas programadas.
- Libros, planes de curso, planes de evaluacion, trabajos practicos, trabajos sustitutivos entro otros.

Noticias UNA CIAP Calabozo se consolida como un recurso esencial para la comunidad universitaria, promoviendo la transparencia, la cercanía y el sentido de pertenencia entre sus miembros. Invitamos a toda la comunidad a visitar nuestra plataforma digital y mantenerse informada sobre las últimas noticias y eventos de la UNA, Núcleo Calabozo.

## ¡Ayudanos a crecer!
Noticias UNA CIAP Calabozo es un proyecto comunitario con un gran espíritu de código abierto. Su mantenimiento y evolución dependen de la colaboración activa de personal universitario y estudiantil. Sin importar tu área de estudio o cargo, puedes contribuir significativamente a este proyecto.

Buscamos personas con diversas habilidades para fortalecer nuestro equipo. Si tienes aptitudes en redacción, administración, codificación o SEO, ¡te invitamos a unirte a nosotros! Tu colaboración es invaluable para mantener Noticias UNA CIAP Calabozo como una fuente de información confiable y actualizada para la comunidad universitaria.

Existen diversas formas de contribuir: puedes escribir artículos, crear contenido multimedia, colaborar en la gestión de la plataforma web o aportar ideas para mejorar su funcionamiento. Cada contribución, sin importar cuán pequeña parezca, es esencial para el crecimiento y éxito de este proyecto.

Si estás interesado en formar parte del equipo de Noticias UNA CIAP Calabozo, no dudes en contactarnos. Puedes dirigirte a nuestra sede en Calabozo o escribirnos a las siguientes direcciones de correo electrónico:

- ciapcalabozo@outlook.com

¡Agradecemos de antemano tu interés en apoyar a Noticias UNA CIAP Calabozo! Juntos podemos construir un espacio informativo valioso para la comunidad universitaria.

## Requerimientos de desarrollo

Para ejecutar el proyecto en ambiente de desarrollo son necesarias las siguientes dependencias: 

- Git.
- Docker Destop.
- GitBash (solo para usuarios de Windows)

## Pasos para la instalcion

**1. Dirigete al directorio de tu preferencia usando la consola:**

```bash
cd "/directorio/de/tu/preferencia"
```

**2. Clona el repositorio:**

```bash
git clone git@github.com:CIAPCalabozoUNA/NoticiasUNACIAPCalabozo.git
```

**2. Crea un archivo llamado .env.dev para las variables de entorno:**
```env
HOST_IP=""127.0.0.1""
POSTGRES_NAME="el valor de tu eleccion"
POSTGRES_USER="el valor de tu eleccion"
POSTGRES_PASSWORD="el valor de tu eleccion"
DB_HOST="127.0.0.1"
SQL_PORT_="5432"
ADMIN_USER="el valor de tu eleccion"
PASSWORD="el valor de tu eleccion"
```

**2. Ejecuta el archivo 'start.sh':**

```bash
./start.sh
```
**Nota:**

- Este codigo solo ha sido probado en los sitemas operativos Linux y MacOS. El uso de Docker en el proyecto puede facilitar la ejecucion del proyecto pero no esta garantizada su correcta ejecucion. En caso de algun inconveniente no dudes en iniciar un issue.
