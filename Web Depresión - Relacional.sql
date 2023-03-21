CREATE TABLE `usuario` (
  `id_usuario` int,
  `id_rol` int,
  `nombres` varchar(255),
  `apellidos` varchar(255),
  `correo` varchar(255),
  `contrasena` varchar(255),
  `cedula` varchar(255),
  `fecha_nacimiento` varchar(255)
);

CREATE TABLE `rol` (
  `id_rol` int,
  `nombre_rol` varchar(255)
);

CREATE TABLE `rol_permisos` (
  `id_rol_permisos` int,
  `id_rol` int,
  `id_permiso` int
);

CREATE TABLE `permiso` (
  `id_permiso` int,
  `nombre` varchar(255)
);

CREATE TABLE `paciente` (
  `id_paciente` int,
  `id_rol` int,
  `nombres` varchar(255),
  `apellidos` varchar(255),
  `correo` varchar(255),
  `contrasena` varchar(255),
  `cedula` varchar(255),
  `fecha_nacimiento` varchar(255)
);

CREATE TABLE `respuesta_depresion` (
  `id_respuesta` int,
  `id_paciente` int,
  `id_video_respuesta` int,
  `id_audio_respuesta` int,
  `nivel_depresion` varchar(255),
  `descripcion` text,
  `fecha_diagnostico` varchar(255),
  `id_entrevista` int
);

CREATE TABLE `formulario` (
  `id_formulario` int,
  `nombre_formulario` varchar(255)
);

CREATE TABLE `paciente_formulario` (
  `id_paciente_formulario` int,
  `id_paciente` int,
  `id_formulario` int,
  `id_entrevista` int
);

CREATE TABLE `preguntas_formualrio` (
  `id_formulario_preguntas` int,
  `id_formulario` int,
  `id_pregunta` int
);

CREATE TABLE `pregunta` (
  `id_pregunta` int,
  `pregunta` text
);

CREATE TABLE `paciente_video` (
  `id_paciente_video` int,
  `id_paciente` int,
  `id_video` int,
  `id_entrevista` int
);

CREATE TABLE `paciente_audio` (
  `id_paciente_audio` int,
  `id_paciente` int,
  `id_audio` int,
  `id_entrevista` int
);

CREATE TABLE `entrevista` (
  `id_entrevista` int,
  `entrevistador` varchar(255),
  `fecha_entrevista` varchar(255)
);

ALTER TABLE `rol` ADD FOREIGN KEY (`id_rol`) REFERENCES `usuario` (`id_rol`);

ALTER TABLE `rol_permisos` ADD FOREIGN KEY (`id_rol`) REFERENCES `rol` (`id_rol`);

ALTER TABLE `rol_permisos` ADD FOREIGN KEY (`id_permiso`) REFERENCES `permiso` (`id_permiso`);

ALTER TABLE `respuesta_depresion` ADD FOREIGN KEY (`id_paciente`) REFERENCES `paciente` (`id_paciente`);

ALTER TABLE `paciente_formulario` ADD FOREIGN KEY (`id_paciente`) REFERENCES `paciente` (`id_paciente`);

ALTER TABLE `paciente_formulario` ADD FOREIGN KEY (`id_formulario`) REFERENCES `formulario` (`id_formulario`);

ALTER TABLE `preguntas_formualrio` ADD FOREIGN KEY (`id_formulario`) REFERENCES `formulario` (`id_formulario`);

ALTER TABLE `preguntas_formualrio` ADD FOREIGN KEY (`id_pregunta`) REFERENCES `pregunta` (`id_pregunta`);

ALTER TABLE `paciente_video` ADD FOREIGN KEY (`id_paciente`) REFERENCES `paciente` (`id_paciente`);

ALTER TABLE `paciente_audio` ADD FOREIGN KEY (`id_paciente`) REFERENCES `paciente` (`id_paciente`);

ALTER TABLE `paciente_audio` ADD FOREIGN KEY (`id_entrevista`) REFERENCES `entrevista` (`id_entrevista`);

ALTER TABLE `paciente_video` ADD FOREIGN KEY (`id_entrevista`) REFERENCES `entrevista` (`id_entrevista`);

ALTER TABLE `paciente_formulario` ADD FOREIGN KEY (`id_entrevista`) REFERENCES `entrevista` (`id_entrevista`);
