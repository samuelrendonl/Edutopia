USE finexcon_edutopia;

SET @role_column_exists = (
  SELECT COUNT(*)
  FROM information_schema.columns
  WHERE table_schema = DATABASE()
    AND table_name = 'parents'
    AND column_name = 'role'
);
SET @role_column_sql = IF(
  @role_column_exists = 0,
  'ALTER TABLE parents ADD COLUMN role VARCHAR(40) NOT NULL DEFAULT ''parent''',
  'SELECT 1'
);
PREPARE add_role_column FROM @role_column_sql;
EXECUTE add_role_column;
DEALLOCATE PREPARE add_role_column;

CREATE TABLE IF NOT EXISTS roles (
  name VARCHAR(40) PRIMARY KEY,
  display_name VARCHAR(80) NOT NULL,
  description VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS permissions (
  name VARCHAR(80) PRIMARY KEY,
  description VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS role_permissions (
  role_name VARCHAR(40) NOT NULL,
  permission_name VARCHAR(80) NOT NULL,
  PRIMARY KEY (role_name, permission_name),
  CONSTRAINT fk_role_permissions_role FOREIGN KEY (role_name) REFERENCES roles(name) ON DELETE CASCADE,
  CONSTRAINT fk_role_permissions_permission FOREIGN KEY (permission_name) REFERENCES permissions(name) ON DELETE CASCADE
);

INSERT IGNORE INTO roles (name, display_name, description) VALUES
  ('parent', 'Familia', 'Gestiona perfiles infantiles y acompaña su progreso.'),
  ('teacher', 'Docente', 'Consulta aprendizajes y progreso de sus estudiantes.'),
  ('editor', 'Editor de contenidos', 'Consulta y administra el catálogo educativo.'),
  ('admin', 'Administrador', 'Acceso completo a usuarios, permisos, catálogo y reportes.');

INSERT IGNORE INTO permissions (name, description) VALUES
  ('learning.view', 'Consultar aprendizajes y juegos del catálogo.'),
  ('learning.manage', 'Administrar contenidos y configuración curricular.'),
  ('children.manage', 'Crear y administrar perfiles infantiles propios.'),
  ('progress.view', 'Consultar avances y resultados.'),
  ('reports.view', 'Consultar métricas y reportes globales.'),
  ('users.manage', 'Consultar usuarios y asignar roles.');

INSERT IGNORE INTO role_permissions (role_name, permission_name) VALUES
  ('parent', 'learning.view'),
  ('parent', 'children.manage'),
  ('parent', 'progress.view'),
  ('teacher', 'learning.view'),
  ('teacher', 'progress.view'),
  ('teacher', 'reports.view'),
  ('editor', 'learning.view'),
  ('editor', 'learning.manage'),
  ('admin', 'learning.view'),
  ('admin', 'learning.manage'),
  ('admin', 'children.manage'),
  ('admin', 'progress.view'),
  ('admin', 'reports.view'),
  ('admin', 'users.manage');
