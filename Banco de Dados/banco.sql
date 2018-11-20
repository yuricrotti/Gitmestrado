-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`usuarios` (
  `id_usuario` INT NOT NULL,
  `nome_usuario` VARCHAR(45) NULL,
  `cargo_usuario` VARCHAR(45) NULL,
  `identificador_usuario` VARCHAR(45) NULL,
  `senha_usuario` VARCHAR(45) NULL,
  `datacad_usuario` DATE NULL,
  `status_usuario` VARCHAR(45) NULL,
  PRIMARY KEY (`id_usuario`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`frutas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`frutas` (
  `id_fruta` INT NOT NULL,
  `nome_fruta` VARCHAR(45) NULL,
  `cultivar_fruta` VARCHAR(45) NULL,
  `lote_fruta` VARCHAR(45) NULL,
  `safra_fruta` DATE NULL,
  `colheita_fruta` DATE NULL,
  `datacad_fruta` DATE NULL,
  `status_fruta` VARCHAR(45) NULL,
  PRIMARY KEY (`id_fruta`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`camaras`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`camaras` (
  `id_camara` INT NOT NULL,
  `posicao_camara` VARCHAR(45) NULL,
  `tamanho_camara` VARCHAR(45) NULL,
  `datacad_camara` DATE NULL,
  `status_camara` VARCHAR(45) NULL,
  PRIMARY KEY (`id_camara`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`atividades`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`atividades` (
  `id_atividade` INT NOT NULL,
  `modoop_atividade` VARCHAR(45) NULL,
  `setpointa_atividade` VARCHAR(45) NULL,
  `setpointb_atividade` VARCHAR(45) NULL,
  `datainicial_atividade` DATE NULL,
  `datafinal_atividade` DATE NULL,
  `datacad_atividade` DATE NULL,
  `status_atividade` VARCHAR(45) NULL,
  `usuarios_id_usuario` INT NOT NULL,
  `frutas_id_fruta` INT NOT NULL,
  `camaras_id_camara` INT NOT NULL,
  PRIMARY KEY (`id_atividade`),
  INDEX `fk_atividades_usuarios_idx` (`usuarios_id_usuario` ASC),
  INDEX `fk_atividades_frutas1_idx` (`frutas_id_fruta` ASC),
  INDEX `fk_atividades_camaras1_idx` (`camaras_id_camara` ASC),
  CONSTRAINT `fk_atividades_usuarios`
    FOREIGN KEY (`usuarios_id_usuario`)
    REFERENCES `mydb`.`usuarios` (`id_usuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_atividades_frutas1`
    FOREIGN KEY (`frutas_id_fruta`)
    REFERENCES `mydb`.`frutas` (`id_fruta`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_atividades_camaras1`
    FOREIGN KEY (`camaras_id_camara`)
    REFERENCES `mydb`.`camaras` (`id_camara`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`qualidades`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`qualidades` (
  `id_qualidade` INT NOT NULL,
  `acidez_qualiade` FLOAT NULL,
  `iiodoamido_qualidade` FLOAT NULL,
  `datacad_qualidade` DATE NULL,
  `qualidadescol` VARCHAR(45) NULL,
  `atividades_id_atividade` INT NOT NULL,
  PRIMARY KEY (`id_qualidade`),
  INDEX `fk_qualidades_atividades1_idx` (`atividades_id_atividade` ASC),
  CONSTRAINT `fk_qualidades_atividades1`
    FOREIGN KEY (`atividades_id_atividade`)
    REFERENCES `mydb`.`atividades` (`id_atividade`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`sensores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`sensores` (
  `id_sensor` INT NOT NULL,
  `nome_sensor` VARCHAR(45) NULL,
  `tipogas_sensor` VARCHAR(45) NULL,
  `datadac_sensor` DATE NULL,
  PRIMARY KEY (`id_sensor`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`dados`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`dados` (
  `id_dado` INT NOT NULL,
  `valor_dado` VARCHAR(45) NULL,
  `datacad_dado` DATE NULL,
  `status_dado` VARCHAR(45) NULL,
  `sensores_id_sensor` INT NOT NULL,
  `atividades_id_atividade` INT NOT NULL,
  PRIMARY KEY (`id_dado`),
  INDEX `fk_dados_sensores1_idx` (`sensores_id_sensor` ASC),
  INDEX `fk_dados_atividades1_idx` (`atividades_id_atividade` ASC),
  CONSTRAINT `fk_dados_sensores1`
    FOREIGN KEY (`sensores_id_sensor`)
    REFERENCES `mydb`.`sensores` (`id_sensor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_dados_atividades1`
    FOREIGN KEY (`atividades_id_atividade`)
    REFERENCES `mydb`.`atividades` (`id_atividade`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
