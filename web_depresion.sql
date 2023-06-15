-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 15-06-2023 a las 06:11:13
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `web_depresion`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$260000$yExS3aJHWXEhGQUUyZpCmd$QJac+fHIPyJuThSCucPWDBXeVFy0xXxgYNZQ1YlTCds=', '2023-02-14 15:25:01.379203', 1, 'admin', '', '', 'admin@admin.com', 1, 1, '2023-02-14 15:24:45.913405');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `diagnostico_phq9`
--

CREATE TABLE `diagnostico_phq9` (
  `id_diagnostico` int(11) NOT NULL,
  `rango1` int(11) NOT NULL,
  `rango2` int(11) NOT NULL,
  `diagnostico` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `diagnostico_phq9`
--

INSERT INTO `diagnostico_phq9` (`id_diagnostico`, `rango1`, `rango2`, `diagnostico`) VALUES
(1, 0, 4, 'Mínimo'),
(2, 5, 9, 'Leve'),
(3, 10, 14, 'Moderado'),
(4, 15, 19, 'Moderado a grave'),
(5, 20, 27, 'Grave');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-02-14 15:19:54.323494'),
(2, 'auth', '0001_initial', '2023-02-14 15:19:55.457867'),
(3, 'admin', '0001_initial', '2023-02-14 15:19:55.631006'),
(4, 'admin', '0002_logentry_remove_auto_add', '2023-02-14 15:19:55.641961'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2023-02-14 15:19:55.650941'),
(6, 'contenttypes', '0002_remove_content_type_name', '2023-02-14 15:19:55.704749'),
(7, 'auth', '0002_alter_permission_name_max_length', '2023-02-14 15:19:55.748632'),
(8, 'auth', '0003_alter_user_email_max_length', '2023-02-14 15:19:55.770576'),
(9, 'auth', '0004_alter_user_username_opts', '2023-02-14 15:19:55.777555'),
(10, 'auth', '0005_alter_user_last_login_null', '2023-02-14 15:19:55.820441'),
(11, 'auth', '0006_require_contenttypes_0002', '2023-02-14 15:19:55.824429'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2023-02-14 15:19:55.835405'),
(13, 'auth', '0008_alter_user_username_max_length', '2023-02-14 15:19:55.851359'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2023-02-14 15:19:55.869373'),
(15, 'auth', '0010_alter_group_name_max_length', '2023-02-14 15:19:55.888258'),
(16, 'auth', '0011_update_proxy_permissions', '2023-02-14 15:19:55.911210'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2023-02-14 15:19:55.931156'),
(18, 'sessions', '0001_initial', '2023-02-14 15:19:56.010388');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('t0kgoz55yus5h299y8x8lpgbpe0yqgnp', '.eJxVjEEOgjAQRe_StWna0hnBpXvO0Mx0poIaSCisjHdXEha6_e-9_zKJtnVIW9UljWIuxpvT78aUHzrtQO403Wab52ldRra7Yg9abT-LPq-H-3cwUB2-dUGKMSM64qhQMrQg2ApS0E4YI6qD0gAGJ9L44FjPXacNZ_AhgHrz_gDuaTfQ:1pRxAz:JILdqqxTagzz1WvF4Vqvv5RH0dxrLQQv1EOACzwYHRg', '2023-02-28 15:25:01.382197');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `entrevista`
--

CREATE TABLE `entrevista` (
  `id_entrevista` int(11) NOT NULL,
  `id_entrevistador` int(11) NOT NULL,
  `fecha_entrevista` timestamp NOT NULL DEFAULT current_timestamp(),
  `diagnostico` text NOT NULL,
  `id_paciente` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `entrevista`
--

INSERT INTO `entrevista` (`id_entrevista`, `id_entrevistador`, `fecha_entrevista`, `diagnostico`, `id_paciente`) VALUES
(1, 7, '2023-06-03 21:14:51', 'Esta mela\r\n', 6),
(2, 7, '2023-06-03 21:42:49', 'Sigue melisisma', 6),
(4, 7, '2023-06-03 21:43:28', 'Dolor de cabeza', 3),
(17, 38, '2023-06-04 18:55:29', 'Este man no tiene nada', 5),
(18, 41, '2023-06-13 14:45:55', 'Esta mejor', 5);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `formulario`
--

CREATE TABLE `formulario` (
  `id_formulario` int(11) NOT NULL,
  `nombre_formulario` varchar(255) DEFAULT NULL,
  `id_paciente` int(11) NOT NULL,
  `puntos` int(11) DEFAULT NULL,
  `diagnostico` text DEFAULT NULL,
  `fecha` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `formulario`
--

INSERT INTO `formulario` (`id_formulario`, `nombre_formulario`, `id_paciente`, `puntos`, `diagnostico`, `fecha`) VALUES
(4, 'Entrevista Manuela Vargas', 6, 1, 'Mínimo', '2023-06-03 19:59:41'),
(6, 'Entrevista juan .', 39, 18, 'Moderado a grave', '2023-06-03 19:59:41'),
(7, 'Entrevista Juan Manuel Restrepo Urrego', 5, 4, 'Mínimo', '2023-06-03 20:38:17'),
(8, 'Entrevista Camilo Erira ', 3, 15, 'Moderado a grave', '2023-06-03 21:43:56'),
(10, 'Entrevista Camilo Erira ', 3, 0, 'Mínimo', '2023-06-13 15:08:14'),
(11, 'Entrevista Camilo Erira ', 3, 1, 'Mínimo', '2023-06-15 02:58:33');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `paciente`
--

CREATE TABLE `paciente` (
  `id_paciente` int(11) NOT NULL,
  `id_rol` int(11) DEFAULT NULL,
  `nombres` varchar(255) DEFAULT NULL,
  `apellidos` varchar(255) DEFAULT NULL,
  `correo` varchar(255) DEFAULT NULL,
  `contrasena` varchar(255) DEFAULT NULL,
  `cedula` varchar(255) DEFAULT NULL,
  `fecha_nacimiento` varchar(255) DEFAULT NULL,
  `activo` bit(1) NOT NULL DEFAULT b'1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `paciente_audio`
--

CREATE TABLE `paciente_audio` (
  `id_paciente_audio` int(11) NOT NULL,
  `id_paciente` int(11) DEFAULT NULL,
  `id_doctor` int(11) NOT NULL,
  `id_audio` text DEFAULT NULL,
  `fecha` timestamp NOT NULL DEFAULT current_timestamp(),
  `diagnostico` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `paciente_audio`
--

INSERT INTO `paciente_audio` (`id_paciente_audio`, `id_paciente`, `id_doctor`, `id_audio`, `fecha`, `diagnostico`) VALUES
(6, 3, 0, '2fd252958f12c1f4b53de13b42533dd7aa4ba066', '2023-06-14 01:42:03', 'Bajo nivel de depresión'),
(7, 3, 0, '678872f2e53ba3e888f689fab377e9eff7425ca6', '2023-06-14 03:36:52', 'Bajo nivel de depresión'),
(8, 3, 0, '8a46d0abbcfeefd86b9b52f05344376535cf12e6', '2023-06-15 02:22:25', 'Alto nivel de depresión'),
(9, 3, 38, 'fc524609b2e6ff2578384accb6db0f3441260b7a', '2023-06-15 02:55:57', 'Bajo nivel de depresión'),
(10, 3, 38, 'cbefd489a87411da906095211d2859b26d3ced87', '2023-06-15 02:57:18', 'Bajo nivel de depresión'),
(11, 3, 38, 'cb7df7a5082f074802373aa392bec728c975552f', '2023-06-15 02:57:44', 'Alto nivel de depresión'),
(12, 6, 38, '58fe68333937323c350190c037598806b8812a99', '2023-06-15 02:59:46', 'Bajo nivel de depresión');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `paciente_video`
--

CREATE TABLE `paciente_video` (
  `id_paciente_video` int(11) NOT NULL,
  `id_paciente` int(11) NOT NULL,
  `id_doctor` int(11) NOT NULL DEFAULT 38,
  `id_video` text DEFAULT NULL,
  `fecha` timestamp NOT NULL DEFAULT current_timestamp(),
  `diagnostico` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `paciente_video`
--

INSERT INTO `paciente_video` (`id_paciente_video`, `id_paciente`, `id_doctor`, `id_video`, `fecha`, `diagnostico`) VALUES
(6, 3, 38, '2fd252958f12c1f4b53de13b42533dd7aa4ba066', '2023-06-14 01:42:03', 'Alto nivel de depresión'),
(7, 3, 38, '678872f2e53ba3e888f689fab377e9eff7425ca6', '2023-06-14 03:36:52', 'Alto nivel de depresión'),
(8, 3, 38, '8a46d0abbcfeefd86b9b52f05344376535cf12e6', '2023-06-15 02:22:25', 'Bajo nivel de depresión'),
(9, 3, 38, 'fc524609b2e6ff2578384accb6db0f3441260b7a', '2023-06-15 02:55:57', 'Alto nivel de depresión'),
(10, 3, 38, 'cbefd489a87411da906095211d2859b26d3ced87', '2023-06-15 02:57:18', 'Alto nivel de depresión'),
(11, 3, 38, 'cb7df7a5082f074802373aa392bec728c975552f', '2023-06-15 02:57:44', 'Bajo nivel de depresión'),
(12, 6, 38, '58fe68333937323c350190c037598806b8812a99', '2023-06-15 02:59:46', 'Alto nivel de depresión');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `permiso`
--

CREATE TABLE `permiso` (
  `id_permiso` int(11) NOT NULL,
  `nombre_permiso` varchar(255) DEFAULT NULL,
  `titulo` varchar(255) NOT NULL,
  `imagen` varchar(255) NOT NULL,
  `enlace` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `permiso`
--

INSERT INTO `permiso` (`id_permiso`, `nombre_permiso`, `titulo`, `imagen`, `enlace`) VALUES
(1, 'Gestionar pacientes', 'Pacientes', '/./static/Imagenes/pacientes.png', '/gestion_pacientes/'),
(4, 'Gestionar doctores', 'Doctores', '/./static/Imagenes/doctores.png', '/gestion_doctores/'),
(5, 'Video-Entrevista', 'Entrevista', '/./static/Imagenes/entrevista.png', '/video/'),
(6, 'Entrevista virtual', 'Entrevista', '/./static/Imagenes/entrevista.png', '/entrevista/');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pregunta`
--

CREATE TABLE `pregunta` (
  `id_pregunta` int(11) DEFAULT NULL,
  `pregunta` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `preguntas_formulario`
--

CREATE TABLE `preguntas_formulario` (
  `id_formulario_preguntas` int(11) NOT NULL,
  `id_formulario` int(11) DEFAULT NULL,
  `pregunta` text DEFAULT NULL,
  `respuesta` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `preguntas_formulario`
--

INSERT INTO `preguntas_formulario` (`id_formulario_preguntas`, `id_formulario`, `pregunta`, `respuesta`) VALUES
(2, 3, 'Poco interés o agrado al hacer las cosas.', 'Más de la mitad de los días'),
(3, 3, 'Se ha sentido triste, deprimido o desesperado.', 'Casi todos los días'),
(4, 3, 'Ha tenido problemas para dormir, mantenerse despierto o duerme demasiado.', 'Varios días'),
(5, 3, 'Se siente cansado o tiene poca energía.', 'Nunca'),
(6, 3, 'Tiene poco o excesivo apetito.', 'Nunca'),
(7, 3, 'Se ha sentido mal consigo mismo, ha sentido que usted es un fracaso o ha sentido que se ha fallado a sí mismo o a su familia.', 'Nunca'),
(8, 3, 'Ha tenido problemas para concentrarse en actividades como leer el periódico o ver televisión.', 'Nunca'),
(9, 3, 'Se mueve o habla tan despacio que otras personas pueden darse cuenta. Está tan inquieto o intranquilo que da vueltas de un lugar a otro más que de costumbre.', 'Nunca'),
(10, 3, 'Ha pensado que estaría mejor muerto o ha deseado hacerse daño de alguna forma.', 'Nunca'),
(11, 4, 'Poco interés o agrado al hacer las cosas.', 'Varios días'),
(12, 4, 'Se ha sentido triste, deprimido o desesperado.', 'Nunca'),
(13, 4, 'Ha tenido problemas para dormir, mantenerse despierto o duerme demasiado.', 'Nunca'),
(14, 4, 'Se siente cansado o tiene poca energía.', 'Nunca'),
(15, 4, 'Tiene poco o excesivo apetito.', 'Nunca'),
(16, 4, 'Se ha sentido mal consigo mismo, ha sentido que usted es un fracaso o ha sentido que se ha fallado a sí mismo o a su familia.', 'Nunca'),
(17, 4, 'Ha tenido problemas para concentrarse en actividades como leer el periódico o ver televisión.', 'Nunca'),
(18, 4, 'Se mueve o habla tan despacio que otras personas pueden darse cuenta. Está tan inquieto o intranquilo que da vueltas de un lugar a otro más que de costumbre.', 'Nunca'),
(19, 4, 'Ha pensado que estaría mejor muerto o ha deseado hacerse daño de alguna forma.', 'Nunca'),
(20, 5, 'Poco interés o agrado al hacer las cosas.', 'Nunca'),
(21, 5, 'Se ha sentido triste, deprimido o desesperado.', 'Nunca'),
(22, 5, 'Ha tenido problemas para dormir, mantenerse despierto o duerme demasiado.', 'Nunca'),
(23, 5, 'Se siente cansado o tiene poca energía.', 'Nunca'),
(24, 5, 'Tiene poco o excesivo apetito.', 'Nunca'),
(25, 5, 'Se ha sentido mal consigo mismo, ha sentido que usted es un fracaso o ha sentido que se ha fallado a sí mismo o a su familia.', 'Nunca'),
(26, 5, 'Ha tenido problemas para concentrarse en actividades como leer el periódico o ver televisión.', 'Nunca'),
(27, 5, 'Se mueve o habla tan despacio que otras personas pueden darse cuenta. Está tan inquieto o intranquilo que da vueltas de un lugar a otro más que de costumbre.', 'Nunca'),
(28, 5, 'Ha pensado que estaría mejor muerto o ha deseado hacerse daño de alguna forma.', 'Nunca'),
(29, 6, 'Poco interés o agrado al hacer las cosas.', 'Más de la mitad de los días'),
(30, 6, 'Se ha sentido triste, deprimido o desesperado.', 'Más de la mitad de los días'),
(31, 6, 'Ha tenido problemas para dormir, mantenerse despierto o duerme demasiado.', 'Casi todos los días'),
(32, 6, 'Se siente cansado o tiene poca energía.', 'Varios días'),
(33, 6, 'Tiene poco o excesivo apetito.', 'Más de la mitad de los días'),
(34, 6, 'Se ha sentido mal consigo mismo, ha sentido que usted es un fracaso o ha sentido que se ha fallado a sí mismo o a su familia.', 'Varios días'),
(35, 6, 'Ha tenido problemas para concentrarse en actividades como leer el periódico o ver televisión.', 'Más de la mitad de los días'),
(36, 6, 'Se mueve o habla tan despacio que otras personas pueden darse cuenta. Está tan inquieto o intranquilo que da vueltas de un lugar a otro más que de costumbre.', 'Más de la mitad de los días'),
(37, 6, 'Ha pensado que estaría mejor muerto o ha deseado hacerse daño de alguna forma.', 'Casi todos los días'),
(38, 7, 'Poco interés o agrado al hacer las cosas.', 'Más de la mitad de los días'),
(39, 7, 'Se ha sentido triste, deprimido o desesperado.', 'Más de la mitad de los días'),
(40, 7, 'Ha tenido problemas para dormir, mantenerse despierto o duerme demasiado.', 'Nunca'),
(41, 7, 'Se siente cansado o tiene poca energía.', 'Nunca'),
(42, 7, 'Tiene poco o excesivo apetito.', 'Nunca'),
(43, 7, 'Se ha sentido mal consigo mismo, ha sentido que usted es un fracaso o ha sentido que se ha fallado a sí mismo o a su familia.', 'Nunca'),
(44, 7, 'Ha tenido problemas para concentrarse en actividades como leer el periódico o ver televisión.', 'Nunca'),
(45, 7, 'Se mueve o habla tan despacio que otras personas pueden darse cuenta. Está tan inquieto o intranquilo que da vueltas de un lugar a otro más que de costumbre.', 'Nunca'),
(46, 7, 'Ha pensado que estaría mejor muerto o ha deseado hacerse daño de alguna forma.', 'Nunca'),
(47, 8, 'Poco interés o agrado al hacer las cosas.', 'Más de la mitad de los días'),
(48, 8, 'Se ha sentido triste, deprimido o desesperado.', 'Más de la mitad de los días'),
(49, 8, 'Ha tenido problemas para dormir, mantenerse despierto o duerme demasiado.', 'Casi todos los días'),
(50, 8, 'Se siente cansado o tiene poca energía.', 'Casi todos los días'),
(51, 8, 'Tiene poco o excesivo apetito.', 'Casi todos los días'),
(52, 8, 'Se ha sentido mal consigo mismo, ha sentido que usted es un fracaso o ha sentido que se ha fallado a sí mismo o a su familia.', 'Más de la mitad de los días'),
(53, 8, 'Ha tenido problemas para concentrarse en actividades como leer el periódico o ver televisión.', 'Nunca'),
(54, 8, 'Se mueve o habla tan despacio que otras personas pueden darse cuenta. Está tan inquieto o intranquilo que da vueltas de un lugar a otro más que de costumbre.', 'Nunca'),
(55, 8, 'Ha pensado que estaría mejor muerto o ha deseado hacerse daño de alguna forma.', 'Nunca'),
(56, 9, 'Poco interés o agrado al hacer las cosas.', 'Más de la mitad de los días'),
(57, 9, 'Se ha sentido triste, deprimido o desesperado.', 'Más de la mitad de los días'),
(58, 9, 'Ha tenido problemas para dormir, mantenerse despierto o duerme demasiado.', 'Nunca'),
(59, 9, 'Se siente cansado o tiene poca energía.', 'Casi todos los días'),
(60, 9, 'Tiene poco o excesivo apetito.', 'Casi todos los días'),
(61, 9, 'Se ha sentido mal consigo mismo, ha sentido que usted es un fracaso o ha sentido que se ha fallado a sí mismo o a su familia.', 'Más de la mitad de los días'),
(62, 9, 'Ha tenido problemas para concentrarse en actividades como leer el periódico o ver televisión.', 'Más de la mitad de los días'),
(63, 9, 'Se mueve o habla tan despacio que otras personas pueden darse cuenta. Está tan inquieto o intranquilo que da vueltas de un lugar a otro más que de costumbre.', 'Más de la mitad de los días'),
(64, 9, 'Ha pensado que estaría mejor muerto o ha deseado hacerse daño de alguna forma.', 'Nunca'),
(65, 10, 'Poco interés o agrado al hacer las cosas.', 'Nunca'),
(66, 10, 'Se ha sentido triste, deprimido o desesperado.', 'Nunca'),
(67, 10, 'Ha tenido problemas para dormir, mantenerse despierto o duerme demasiado.', 'Nunca'),
(68, 10, 'Se siente cansado o tiene poca energía.', 'Nunca'),
(69, 10, 'Tiene poco o excesivo apetito.', 'Nunca'),
(70, 10, 'Se ha sentido mal consigo mismo, ha sentido que usted es un fracaso o ha sentido que se ha fallado a sí mismo o a su familia.', 'Nunca'),
(71, 10, 'Ha tenido problemas para concentrarse en actividades como leer el periódico o ver televisión.', 'Nunca'),
(72, 10, 'Se mueve o habla tan despacio que otras personas pueden darse cuenta. Está tan inquieto o intranquilo que da vueltas de un lugar a otro más que de costumbre.', 'Nunca'),
(73, 10, 'Ha pensado que estaría mejor muerto o ha deseado hacerse daño de alguna forma.', 'Nunca'),
(74, 11, 'Poco interés o agrado al hacer las cosas.', 'Nunca'),
(75, 11, 'Se ha sentido triste, deprimido o desesperado.', 'Nunca'),
(76, 11, 'Ha tenido problemas para dormir, mantenerse despierto o duerme demasiado.', 'Varios días'),
(77, 11, 'Se siente cansado o tiene poca energía.', 'Nunca'),
(78, 11, 'Tiene poco o excesivo apetito.', 'Nunca'),
(79, 11, 'Se ha sentido mal consigo mismo, ha sentido que usted es un fracaso o ha sentido que se ha fallado a sí mismo o a su familia.', 'Nunca'),
(80, 11, 'Ha tenido problemas para concentrarse en actividades como leer el periódico o ver televisión.', 'Nunca'),
(81, 11, 'Se mueve o habla tan despacio que otras personas pueden darse cuenta. Está tan inquieto o intranquilo que da vueltas de un lugar a otro más que de costumbre.', 'Nunca'),
(82, 11, 'Ha pensado que estaría mejor muerto o ha deseado hacerse daño de alguna forma.', 'Nunca');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `respuestas_phq9`
--

CREATE TABLE `respuestas_phq9` (
  `id_respuesta` int(11) NOT NULL,
  `respuesta` text NOT NULL,
  `valor` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `respuestas_phq9`
--

INSERT INTO `respuestas_phq9` (`id_respuesta`, `respuesta`, `valor`) VALUES
(1, 'Nunca', 0),
(2, 'Varios días', 1),
(3, 'Más de la mitad de los días', 2),
(4, 'Casi todos los días', 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `respuesta_depresion`
--

CREATE TABLE `respuesta_depresion` (
  `id_respuesta` int(11) DEFAULT NULL,
  `id_paciente` int(11) DEFAULT NULL,
  `id_video_respuesta` int(11) DEFAULT NULL,
  `id_audio_respuesta` int(11) DEFAULT NULL,
  `nivel_depresion` varchar(255) DEFAULT NULL,
  `descripcion` text DEFAULT NULL,
  `fecha_diagnostico` varchar(255) DEFAULT NULL,
  `id_entrevista` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rol`
--

CREATE TABLE `rol` (
  `id_rol` int(11) NOT NULL,
  `nombre_rol` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `rol`
--

INSERT INTO `rol` (`id_rol`, `nombre_rol`) VALUES
(1, 'Admin'),
(2, 'Doctor'),
(3, 'Paciente');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rol_permisos`
--

CREATE TABLE `rol_permisos` (
  `id_rol_permisos` int(11) NOT NULL,
  `id_rol` int(11) DEFAULT NULL,
  `id_permiso` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `rol_permisos`
--

INSERT INTO `rol_permisos` (`id_rol_permisos`, `id_rol`, `id_permiso`) VALUES
(1, 1, 1),
(2, 1, 4),
(3, 1, 5),
(4, 1, 6),
(6, 3, 6),
(7, 2, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `test_phq9`
--

CREATE TABLE `test_phq9` (
  `id_test` int(11) NOT NULL,
  `pregunta` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `test_phq9`
--

INSERT INTO `test_phq9` (`id_test`, `pregunta`) VALUES
(1, 'Poco interés o agrado al hacer las cosas.'),
(2, 'Se ha sentido triste, deprimido o desesperado.'),
(3, 'Ha tenido problemas para dormir, mantenerse despierto o duerme demasiado.'),
(4, 'Se siente cansado o tiene poca energía.'),
(5, 'Tiene poco o excesivo apetito.'),
(6, 'Se ha sentido mal consigo mismo, ha sentido que usted es un fracaso o ha sentido que se ha fallado a sí mismo o a su familia.'),
(7, 'Ha tenido problemas para concentrarse en actividades como leer el periódico o ver televisión.'),
(8, 'Se mueve o habla tan despacio que otras personas pueden darse cuenta. Está tan inquieto o intranquilo que da vueltas de un lugar a otro más que de costumbre.'),
(9, 'Ha pensado que estaría mejor muerto o ha deseado hacerse daño de alguna forma.');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id_usuario` int(11) NOT NULL,
  `id_rol` int(11) DEFAULT NULL,
  `nombres` varchar(255) DEFAULT NULL,
  `apellidos` varchar(255) DEFAULT NULL,
  `correo` varchar(255) DEFAULT NULL,
  `direccion` varchar(255) NOT NULL,
  `telefono` varchar(255) NOT NULL,
  `contrasena` varchar(500) DEFAULT NULL,
  `cedula` varchar(255) DEFAULT NULL,
  `fecha_nacimiento` varchar(255) DEFAULT NULL,
  `genero` varchar(255) NOT NULL,
  `activo` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id_usuario`, `id_rol`, `nombres`, `apellidos`, `correo`, `direccion`, `telefono`, `contrasena`, `cedula`, `fecha_nacimiento`, `genero`, `activo`) VALUES
(1, 1, 'Juan ', 'Jose', 'juanjose.aroca@utp.edu.co', 'cr 7 no 23-12', '3228752890', '2a2bdce39e466bac8c982ab2383f266fcbeb07ddaddd92a8e3e3ff07bef73377', '1192713043', '2000-02-14', 'Masculino', 1),
(3, 3, 'Camilo', 'Erira ', 'camilo.erira@utp.edu.co', 'Pasto', '3568979999', '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5', '100023556', '1999-01-01', 'Masculino', 1),
(5, 3, 'Juan Manuel', 'Restrepo Urrego', 'juanmanuel.restrepo@utp.edu.co', 'Vallenato ', '555555555', '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5', '555555', '2002-02-16', 'Masculino', 1),
(6, 3, 'Manuela', 'Vargas', 'manu@ucp.com', 'Tu corazón de melón', '3228752890', '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5', '10235659', '2000-09-13', 'Femenino', 1),
(7, 2, 'Shakira', 'Karol G', 'shakira@gmail.com', 'Barcelona', '350000233', '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5', '10002232222', '1990-02-23', 'Femenino', 1),
(8, 2, 'Usuariobaaf2', 'Apellidoc7136', 'usuario58bff@example.com', 'Direccióne512f', 'c4571d806', '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5', 'e6ab1b0e79', '2000-01-01', 'Masculino', 1),
(9, 2, 'Usuarioee9de', 'Apellidod19ef', 'usuario7cff5@example.com', 'Dirección8d4bf', 'fb4c8a125', '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5', 'ac22afc13e', '2000-01-01', 'Masculino', 1),
(10, 2, 'Usuariod1438', 'Apellidoa858f', 'usuarioe1c96@example.com', 'Direcciónab843', '9b61ecc7d', '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5', 'ed57cafccf', '2000-01-01', 'Masculino', 1),
(11, 2, 'Usuario43526', 'Apellido6c6c1', 'usuario47ae1@example.com', 'Dirección64790', 'fd5c6dd0a', '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5', 'e8ab6fec20', '2000-01-01', 'Masculino', 1),
(12, 2, 'Usuario731c7', 'Apellidof892f', 'usuario73fd8@example.com', 'Dirección3b6f8', '916782e61', '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5', '72421857e9', '2000-01-01', 'Masculino', 1),
(13, 2, 'Usuario68946', 'Apellidod81ec', 'usuariof9800@example.com', 'Dirección359f1', '988d2a8b6', '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5', '4a245b47da', '2000-01-01', 'Masculino', 1),
(14, 2, 'Usuariofc999', 'Apellido370e5', 'usuario8393b@example.com', 'Dirección0577f', '5ea717dca', '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5', '5a32eb52a0', '2000-01-01', 'Masculino', 1),
(15, 2, 'Usuario3379b', 'Apellido15e52', 'usuario4d9e4@example.com', 'Dirección42412', 'f46018afb', '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5', 'd610cfe7c5', '2000-01-01', 'Masculino', 1),
(16, 2, 'Usuario4e8da', 'Apellido15907', 'usuarioe9fb8@example.com', 'Dirección3ff00', 'b1e802c1b', '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5', '83b9fed2b2', '2000-01-01', 'Masculino', 1),
(17, 2, 'Usuariof16da', 'Apellidoc5186', 'usuariof3e4f@example.com', 'Dirección10e97', '873f3d801', '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5', '9a0dca3672', '2000-01-01', 'Masculino', 1),
(18, 2, 'Usuario26a36', 'Apellido5fe1d', 'usuario912d7@example.com', 'Dirección4077e', '1a581c13a', '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5', '6acfe21c2f', '2000-01-01', 'Masculino', 1),
(19, 2, 'Usuario98293', 'Apellido9ba72', 'usuario46b6f@example.com', 'Dirección4473b', '7515ad505', '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5', '9ea6246227', '2000-01-01', 'Masculino', 1),
(20, 2, 'Usuarioc96f1', 'Apellido29e56', 'usuarioffc94@example.com', 'Direcciónf1da3', '459735b97', '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5', '2a487c7458', '2000-01-01', 'Masculino', 1),
(21, 2, 'Usuario86fa4', 'Apellido45c22', 'usuario351cd@example.com', 'Direcciónfed23', '79c481ab7', '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5', '64258073d1', '2000-01-01', 'Masculino', 1),
(22, 2, 'Usuariod340c', 'Apellido1bd79', 'usuario68591@example.com', 'Dirección85ebb', '396f0eb6f', '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5', '2569229d1c', '2000-01-01', 'Masculino', 1),
(23, 3, 'Kmilo', 'Otro', 'usuario0e514@example.com', 'Direcciónd55a6', '000b67afd', '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5', 'e5a4f50cce', '2000-01-01', 'Masculino', 1),
(24, 3, 'Usuarioa2843', 'Apellido8358a', 'usuario7d9d6@example.com', 'Dirección1cd60', '5d1eaaba6', '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5', '89f31520f8', '2000-01-01', 'Masculino', 1),
(25, 3, 'Usuario798d7', 'Apellidof607c', 'usuario5a4bf@example.com', 'Dirección3ff6c', '623701ce3', '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5', '62f836b40a', '2000-01-01', 'Masculino', 1),
(26, 3, 'Usuariocbdd3', 'Apellido137fb', 'usuariof7555@example.com', 'Dirección714fd', 'cde35f2b0', '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5', '2b8b6112ec', '2000-01-01', 'Masculino', 1),
(27, 3, 'Usuarioa2c1c', 'Apellidoc35ed', 'usuario7a9de@example.com', 'Dirección3f9a0', 'a0fc8969f', '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5', '46af415731', '2000-01-01', 'Masculino', 1),
(28, 3, 'Usuario19db3', 'Apellidoc6100', 'usuario123c8@example.com', 'Dirección210aa', 'efa868039', '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5', '906efb047f', '2000-01-01', 'Masculino', 1),
(29, 3, 'Usuario0b9b5', 'Apellido77301', 'usuarioe031a@example.com', 'Dirección54957', '48293bfef', '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5', 'b65958d0a0', '2000-01-01', 'Masculino', 1),
(30, 3, 'Usuariob0d67', 'Apellidoee722', 'usuario224ee@example.com', 'Dirección15cf2', '5ccc5d64e', '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5', 'a8d97fcf0f', '2000-01-01', 'Masculino', 1),
(31, 3, 'Usuario6af52', 'Apellidoe6f10', 'usuario8e559@example.com', 'Direcciónd54c4', '66fd36d9e', '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5', 'f8e3654c5b', '2000-01-01', 'Masculino', 1),
(32, 3, 'Usuario8b154', 'Apellidodfa97', 'usuariocb1ad@example.com', 'Dirección0030a', '768dc1cb1', '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5', '00be1871b3', '2000-01-01', 'Masculino', 1),
(33, 3, 'Usuariob8140', 'Apellido333c4', 'usuariocd079@example.com', 'Dirección5d357', '9577ead26', '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5', 'bbe61ab622', '2000-01-01', 'Masculino', 1),
(34, 3, 'Usuario7d765', 'Apellidocb896', 'usuario1fdd5@example.com', 'Dirección65d17', 'e60a962ff', '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5', 'fb2ebc6e79', '2000-01-01', 'Masculino', 1),
(35, 3, 'Usuario10826', 'Apellido85590', 'usuarioa549b@example.com', 'Direcciónf90c2', '87a0a638d', '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5', '6060e5badc', '2000-01-01', 'Masculino', 1),
(36, 3, 'Usuario77d52', 'Apellido18c94', 'usuario04c52@example.com', 'Dirección3ca0a', '2175ad490', '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5', '7b26d067e7', '2000-01-01', 'Masculino', 1),
(37, 3, 'Usuario6595c', 'Apellidoec405', 'usuariofec73@example.com', 'Dirección73ffe', 'e53f25d77', '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5', 'a715e9157b', '2000-01-01', 'Masculino', 1),
(38, 2, 'Ana María', 'López', 'anamayi@utp.edu.co', 'Pereira', '3333', '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5', '102369999', '1990-01-01', 'Femenino', 1),
(39, 3, 'juan', '.', 'juan@gmail.com', 'Tu corazón', '55555', '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5', '102359887898', '2000-01-01', 'Masculino', 1),
(40, 2, 'jose', 'jose', 'jose@gmail.com', '', '', '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5', '1000000000000', '1999-01-01', 'Masculino', 1),
(41, 2, 'Juan Manuel', 'velazquez', 'jumavefes@utp.edu.co', 'utp', '3222558989', '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5', '14854995999', '1990-01-01', 'Masculino', 1);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indices de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indices de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `diagnostico_phq9`
--
ALTER TABLE `diagnostico_phq9`
  ADD PRIMARY KEY (`id_diagnostico`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indices de la tabla `entrevista`
--
ALTER TABLE `entrevista`
  ADD PRIMARY KEY (`id_entrevista`);

--
-- Indices de la tabla `formulario`
--
ALTER TABLE `formulario`
  ADD PRIMARY KEY (`id_formulario`);

--
-- Indices de la tabla `paciente`
--
ALTER TABLE `paciente`
  ADD PRIMARY KEY (`id_paciente`);

--
-- Indices de la tabla `paciente_audio`
--
ALTER TABLE `paciente_audio`
  ADD PRIMARY KEY (`id_paciente_audio`);

--
-- Indices de la tabla `paciente_video`
--
ALTER TABLE `paciente_video`
  ADD PRIMARY KEY (`id_paciente_video`);

--
-- Indices de la tabla `permiso`
--
ALTER TABLE `permiso`
  ADD PRIMARY KEY (`id_permiso`);

--
-- Indices de la tabla `preguntas_formulario`
--
ALTER TABLE `preguntas_formulario`
  ADD PRIMARY KEY (`id_formulario_preguntas`);

--
-- Indices de la tabla `respuestas_phq9`
--
ALTER TABLE `respuestas_phq9`
  ADD PRIMARY KEY (`id_respuesta`);

--
-- Indices de la tabla `rol`
--
ALTER TABLE `rol`
  ADD PRIMARY KEY (`id_rol`);

--
-- Indices de la tabla `rol_permisos`
--
ALTER TABLE `rol_permisos`
  ADD PRIMARY KEY (`id_rol_permisos`);

--
-- Indices de la tabla `test_phq9`
--
ALTER TABLE `test_phq9`
  ADD PRIMARY KEY (`id_test`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id_usuario`),
  ADD UNIQUE KEY `correo` (`correo`),
  ADD UNIQUE KEY `cedula` (`cedula`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `diagnostico_phq9`
--
ALTER TABLE `diagnostico_phq9`
  MODIFY `id_diagnostico` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT de la tabla `entrevista`
--
ALTER TABLE `entrevista`
  MODIFY `id_entrevista` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT de la tabla `formulario`
--
ALTER TABLE `formulario`
  MODIFY `id_formulario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de la tabla `paciente`
--
ALTER TABLE `paciente`
  MODIFY `id_paciente` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `paciente_audio`
--
ALTER TABLE `paciente_audio`
  MODIFY `id_paciente_audio` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `paciente_video`
--
ALTER TABLE `paciente_video`
  MODIFY `id_paciente_video` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `permiso`
--
ALTER TABLE `permiso`
  MODIFY `id_permiso` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `preguntas_formulario`
--
ALTER TABLE `preguntas_formulario`
  MODIFY `id_formulario_preguntas` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=83;

--
-- AUTO_INCREMENT de la tabla `respuestas_phq9`
--
ALTER TABLE `respuestas_phq9`
  MODIFY `id_respuesta` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `rol`
--
ALTER TABLE `rol`
  MODIFY `id_rol` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `rol_permisos`
--
ALTER TABLE `rol_permisos`
  MODIFY `id_rol_permisos` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `test_phq9`
--
ALTER TABLE `test_phq9`
  MODIFY `id_test` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=42;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
