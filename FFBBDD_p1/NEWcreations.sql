DROP TABLE Ficha;
DROP TABLE Pista;
DROP TABLE Album;
DROP TABLE Interpreta;
DROP TABLE Tema;
DROP TABLE Concierto;
DROP TABLE Gira;
DROP TABLE Asistente;
DROP TABLE Estudio;
DROP TABLE Discografica;
DROP TABLE Manager;
DROP TABLE Pertenece;
DROP TABLE Musico;
DROP TABLE Interprete;


CREATE TABLE Interprete (
    nombre VARCHAR2(50),
    nacionalidad VARCHAR2(20) NOT NULL,
    idioma VARCHAR2(20) NOT NULL,
    CONSTRAINT pk_interprete PRIMARY KEY (nombre)
);


CREATE TABLE Musico (
    pasaporte VARCHAR2(14),
    nombre_completo VARCHAR2(50) NOT NULL,
    nacionalidad VARCHAR2(20) NOT NULL,
    birthdate DATE NOT NULL,
    CONSTRAINT pk_musico PRIMARY KEY (pasaporte)
);

CREATE TABLE Pertenece (
    musico VARCHAR(14),
    interprete VARCHAR(50),
    rol VARCHAR2(15) NOT NULL,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE,
    CONSTRAINT pk_pertenece PRIMARY KEY (musico, interprete),
    CONSTRAINT fk_pertenece_musico FOREIGN KEY (musico) REFERENCES Musico(pasaporte) ON DELETE CASCADE,
    CONSTRAINT fk_pertenece_interprete FOREIGN KEY (interprete) REFERENCES Interprete(nombre) ON DELETE CASCADE,
    CONSTRAINT ck_fechaInicio CHECK (fecha_inicio < fecha_fin)	
);

CREATE TABLE Manager (
    telefono NUMBER(9),
    nombre VARCHAR2(35) NOT NULL,
    apellido1 VARCHAR2(20) NOT NULL,
    apellido2 VARCHAR2(20),
    CONSTRAINT pk_manager PRIMARY KEY (telefono)
);

CREATE TABLE Discografica (
    nombre VARCHAR2(25),
    telefono NUMBER(10) NOT NULL,
    CONSTRAINT pk_discografica PRIMARY KEY (nombre)
);

CREATE TABLE Estudio (
    nombre VARCHAR2(50),
    direccion VARCHAR2(100) NOT NULL,
    CONSTRAINT pk_estudio PRIMARY KEY (nombre)
);

CREATE TABLE Asistente (
    email VARCHAR2(100),
    pasaporte VARCHAR2(8),
    nombre VARCHAR2(80),
    apellido1 VARCHAR2(80),
    apellido2 VARCHAR2(80),
    nacimiento DATE,
    telefono NUMBER(10),
    direccion VARCHAR2(100),
    CONSTRAINT pk_asistente PRIMARY KEY (email),
    CONSTRAINT sk_asistente UNIQUE (pasaporte)
);

CREATE TABLE Gira (
    artista VARCHAR2(50),
    nombre VARCHAR2(100),
    manager NUMBER(10) NOT NULL,
    CONSTRAINT pk_gira PRIMARY KEY (artista, nombre),
    CONSTRAINT fk_gira_artista FOREIGN KEY (artista) REFERENCES Interprete(nombre) ON DELETE CASCADE,
    CONSTRAINT fk_gira_manager FOREIGN KEY (manager) REFERENCES Manager(telefono) ON DELETE CASCADE
);

CREATE TABLE  Concierto (
    interprete VARCHAR2(50),
    fecha DATE,
    municipio VARCHAR2(100) NOT NULL,
    pais VARCHAR2(100) NOT NULL,
    gira_artista VARCHAR2(100),
    gira_nombre VARCHAR2(100),
    manager NUMBER(10) NOT NULL,
    duracion NUMBER(4),
    direccion VARCHAR2(100) NOT NULL,
    asistentes number(7),
    CONSTRAINT pk_concierto PRIMARY KEY (interprete, fecha),
    CONSTRAINT fk_concierto_interprete FOREIGN KEY (interprete) REFERENCES Interprete(nombre),
    CONSTRAINT fk_concierto_gira FOREIGN KEY (gira_artista, gira_nombre) REFERENCES Gira(artista, nombre) ON DELETE SET NULL,
    CONSTRAINT fk_concierto_manager FOREIGN KEY (manager) REFERENCES Manager(telefono)
);

CREATE TABLE Tema (
    titulo VARCHAR2(50),
    autor VARCHAR2(50),
    autor2 VARCHAR2(50),
    CONSTRAINT pk_temas PRIMARY KEY (titulo, autor),
    CONSTRAINT fk_temas_autor FOREIGN KEY (autor) REFERENCES Musico(pasaporte) ON DELETE CASCADE,
    CONSTRAINT fk_temas_autor2 FOREIGN KEY (autor2) REFERENCES Musico(pasaporte) ON DELETE SET NULL
);

CREATE TABLE Interpreta (
    tema_titulo VARCHAR2(50) NOT NULL,
    tema_autor VARCHAR2(50) NOT NULL,
    concierto_interprete VARCHAR2(50),
    concierto_fecha DATE,
    duracion VARCHAR2(4),
    seq NUMBER(3),
    CONSTRAINT pk_interpreta PRIMARY KEY (seq, concierto_interprete, concierto_fecha), 
    -- Una interpretacion la caracteriza el lugar en la secuencia y el concierto donde se interpreto la pista
    CONSTRAINT fk_interpreta_concierto FOREIGN KEY (concierto_interprete, concierto_fecha) REFERENCES Concierto(interprete, fecha) ON DELETE CASCADE,
    CONSTRAINT fk_interpreta_tema FOREIGN KEY (tema_titulo, tema_autor) REFERENCES Tema(titulo, autor)
);

CREATE TABLE Album (
    pair VARCHAR2(15),
    fecha DATE NOT NULL,
    formato VARCHAR2(10) NOT NULL,
    discografica VARCHAR2(25) NOT NULL,
    interprete VARCHAR2(50) NOT NULL,
    titulo VARCHAR2(50) NOT NULL, 
    duracion NUMBER(10) NOT NULL,
    manager number(10),
    CONSTRAINT pk_album PRIMARY KEY (pair),
    CONSTRAINT sk_album_fechaFormato UNIQUE (pair, fecha, formato),
    CONSTRAINT fk_album_discografica FOREIGN KEY (discografica) REFERENCES Discografica(nombre),
    CONSTRAINT fK_album_interprete FOREIGN KEY (interprete) REFERENCES Interprete(nombre) ON DELETE CASCADE,
    CONSTRAINT fk_album_manager FOREIGN KEY (manager) REFERENCES Manager(telefono) ON DELETE SET NULL
);

CREATE TABLE Pista ( 
    album VARCHAR2(15),
    num NUMBER(2), 
    tema_titulo VARCHAR2(100) NOT NULL,
    tema_autor VARCHAR2(50) NOT NULL,
    fecha_grab DATE NOT NULL,
    estudio VARCHAR2(50),
    ingeniero VARCHAR2(50) NOT NULL,
    duracion number(4) NOT NULL,
    CONSTRAINT pk_pista PRIMARY KEY (album, num),
    CONSTRAINT fk_pista_tema FOREIGN KEY (tema_titulo, tema_autor) REFERENCES Tema(titulo, autor) ON DELETE CASCADE,
    CONSTRAINT fk_pista_estudio FOREIGN KEY (estudio) REFERENCES Estudio(nombre) ON DELETE SET NULL,
    CONSTRAINT fk_pista_album FOREIGN KEY (album) REFERENCES Album(pair) ON DELETE CASCADE
);

CREATE TABLE Ficha (
    rfid VARCHAR2(120),
    cliente VARCHAR(100) NOT NULL,
    evento_interprete VARCHAR2(50) NOT NULL,
    evento_fecha DATE NOT NULL,
    fecha_compra DATE NOT NULL,
    fecha_cliente DATE NOT NULL,
    CONSTRAINT pk_ficha PRIMARY KEY (rfid),
    CONSTRAINT sk_ficha_eventoCliente UNIQUE (evento_interprete, evento_fecha, cliente),
    CONSTRAINT fk_ficha_asistente FOREIGN KEY (cliente) REFERENCES Asistente(email) ON DELETE CASCADE,
    CONSTRAINT fk_ficha_evento FOREIGN KEY (evento_interprete, evento_fecha) REFERENCES Concierto(interprete, fecha),
    CONSTRAINT ck_edad CHECK (fecha_cliente < fecha_compra - 18*365),
    CONSTRAINT ck_fecha_evento CHECK (evento_fecha > fecha_compra)
);

-- ==================

DESC Interprete;
DESC Musico;
DESC Pertenece;
DESC Manager;
DESC Discografica;
DESC Estudio;
DESC Asistente;
DESC Gira;
DESC Concierto;
DESC Tema;
DESC Interpreta;
DESC Album;
DESC Pista;
DESC Ficha;


