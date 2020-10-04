-- import to SQLite by running: sqlite3.exe db.sqlite3 -init sqlite.sql

PRAGMA journal_mode = MEMORY;
PRAGMA synchronous = OFF;
PRAGMA foreign_keys = OFF;
PRAGMA ignore_check_constraints = OFF;
PRAGMA auto_vacuum = NONE;
PRAGMA secure_delete = OFF;
BEGIN TRANSACTION;

CREATE TABLE 'itens' (
'cod_item' INTEGER NOT NULL,
'cod_item_pai' INTEGER DEFAULT NULL,
'tipo_item' char(1) NOT NULL,
'nome' TEXT NOT NULL,
'situacao' char(1) NOT NULL DEFAULT 'A',
'dat_inclusao' date NOT NULL,
'usu_inclusao' TEXT NOT NULL,
'dat_alteracao' datetime DEFAULT NULL,
'usu_alteracao' TEXT DEFAULT NULL,
PRIMARY KEY ('cod_item','tipo_item'),
FOREIGN KEY ('cod_item_pai', 'tipo_item') REFERENCES 'itens' ('cod_item', 'tipo_item') ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE 'classes' (
'cod_classe' INTEGER NOT NULL,
'natureza' TEXT DEFAULT NULL,
'dispositivo_legal' TEXT DEFAULT NULL,
'artigo' TEXT DEFAULT NULL,
'sigla' TEXT NOT NULL,
'sigla_antiga' TEXT DEFAULT NULL,
'polo_ativo' TEXT NOT NULL,
'polo_passivo' TEXT NOT NULL,
'glossario' text,
'numeracao_propria' char(1) NOT NULL DEFAULT 'S',
'just_es_1grau' char(1) DEFAULT 'N',
'just_es_2grau' char(1) DEFAULT 'N',
'just_es_juizado_es' char(1) DEFAULT 'N',
'just_es_turmas' char(1) DEFAULT 'N',
'just_es_1grau_mil' char(1) DEFAULT 'N',
'just_es_2grau_mil' char(1) DEFAULT 'N',
'just_es_juizado_es_fp' char(1) DEFAULT 'N',
'just_tu_es_un' char(1) DEFAULT 'N',
'just_fed_1grau' char(1) DEFAULT 'N',
'just_fed_2grau' char(1) DEFAULT 'N',
'just_fed_juizado_es' char(1) DEFAULT 'N',
'just_fed_turmas' char(1) DEFAULT 'N',
'just_fed_nacional' char(1) DEFAULT 'N',
'just_fed_regional' char(1) DEFAULT 'N',
'just_trab_1grau' char(1) DEFAULT 'N',
'just_trab_2grau' char(1) DEFAULT 'N',
'just_trab_tst' char(1) DEFAULT 'N',
'just_trab_csjt' TEXT  DEFAULT 'N' ,
'stf' char(1) DEFAULT 'N',
'stj' char(1) DEFAULT 'N',
'cjf' char(1) DEFAULT 'N',
'cnj' char(1) DEFAULT 'N',
'just_mil_uniao_1grau' char(1) DEFAULT 'N',
'just_mil_uniao_stm' char(1) DEFAULT 'N',
'just_mil_est_1grau' char(1) DEFAULT 'N',
'just_mil_est_tjm' char(1) DEFAULT 'N',
'just_elei_1grau' char(1) DEFAULT 'N',
'just_elei_2grau' char(1) DEFAULT 'N',
'just_elei_tse' char(1) DEFAULT 'N',
'tipo_item' char(1) NOT NULL DEFAULT 'C',
'usu_inclusao' TEXT DEFAULT NULL,
'dat_inclusao' datetime DEFAULT NULL,
'dsc_ip_usu_inclusao' TEXT DEFAULT NULL,
'usu_alteracao' TEXT DEFAULT NULL,
PRIMARY KEY ('cod_classe'),
FOREIGN KEY ('cod_classe', 'tipo_item') REFERENCES 'itens' ('cod_item', 'tipo_item') ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE 'assuntos' (
'cod_assunto' INTEGER NOT NULL,
'dispositivo_legal' TEXT DEFAULT NULL,
'artigo' TEXT DEFAULT NULL,
'glossario' text,
'sigiloso' char(1) DEFAULT NULL,
'assunto_secundario' char(1) DEFAULT NULL,
'crime_antecedente' char(1) DEFAULT 'N',
'just_es_1grau' char(1) DEFAULT 'N',
'just_es_2grau' char(1) DEFAULT 'N',
'just_es_juizado_es' char(1) DEFAULT 'N',
'just_es_turmas' char(1) DEFAULT 'N',
'just_es_1grau_mil' char(1) DEFAULT 'N',
'just_es_2grau_mil' char(1) DEFAULT 'N',
'just_es_juizado_es_fp' char(1) DEFAULT 'N',
'just_tu_es_un' char(1) DEFAULT 'N',
'just_fed_1grau' char(1) DEFAULT 'N',
'just_fed_2grau' char(1) DEFAULT 'N',
'just_fed_juizado_es' char(1) DEFAULT 'N',
'just_fed_turmas' char(1) DEFAULT 'N',
'just_fed_nacional' char(1) DEFAULT 'N',
'just_fed_regional' char(1) DEFAULT 'N',
'just_trab_1grau' char(1) DEFAULT 'N',
'just_trab_2grau' char(1) DEFAULT 'N',
'just_trab_tst' char(1) DEFAULT 'N',
'just_trab_csjt' TEXT  DEFAULT 'N' ,
'stf' char(1) DEFAULT 'N',
'stj' char(1) DEFAULT 'N',
'cjf' char(1) DEFAULT 'N',
'cnj' char(1) DEFAULT 'N',
'just_mil_uniao_1grau' char(1) DEFAULT 'N',
'just_mil_uniao_stm' char(1) DEFAULT 'N',
'just_mil_est_1grau' char(1) DEFAULT 'N',
'just_mil_est_tjm' char(1) DEFAULT 'N',
'just_elei_1grau' char(1) DEFAULT 'N',
'just_elei_2grau' char(1) DEFAULT 'N',
'just_elei_tse' char(1) DEFAULT 'N',
'tipo_item' char(1) NOT NULL DEFAULT 'A',
'usu_inclusao' TEXT DEFAULT NULL,
'dat_inclusao' datetime DEFAULT NULL,
'dsc_ip_usu_inclusao' TEXT DEFAULT NULL,
'usu_alteracao' TEXT DEFAULT NULL,
PRIMARY KEY ('cod_assunto'),
FOREIGN KEY ('cod_assunto', 'tipo_item') REFERENCES 'itens' ('cod_item', 'tipo_item') ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE 'movimentos' (
'cod_movimento' INTEGER NOT NULL,
'movimento' TEXT DEFAULT NULL,
'visibilidade_externa' char(1) DEFAULT NULL,
'monocratico' char(1) DEFAULT NULL,
'colegiado' char(1) DEFAULT NULL,
'presidente_vice' char(1) DEFAULT NULL,
'flg_papel' char(1) DEFAULT NULL,
'flg_eletronico' char(1) DEFAULT 'N',
'dispositivo_legal' TEXT DEFAULT NULL,
'artigo' TEXT DEFAULT NULL,
'glossario' text,
'just_es_1grau' char(1) DEFAULT 'N',
'just_es_2grau' char(1) DEFAULT 'N',
'just_es_juizado_es' char(1) DEFAULT 'N',
'just_es_turmas' char(1) DEFAULT 'N',
'just_es_1grau_mil' char(1) DEFAULT 'N',
'just_es_2grau_mil' char(1) DEFAULT 'N',
'just_es_juizado_es_fp' char(1) DEFAULT 'N',
'just_tu_es_un' char(1) DEFAULT 'N',
'just_fed_1grau' char(1) DEFAULT 'N',
'just_fed_2grau' char(1) DEFAULT 'N',
'just_fed_juizado_es' char(1) DEFAULT 'N',
'just_fed_turmas' char(1) DEFAULT 'N',
'just_fed_nacional' char(1) DEFAULT 'N',
'just_fed_regional' char(1) DEFAULT 'N',
'just_trab_1grau' char(1) DEFAULT 'N',
'just_trab_2grau' char(1) DEFAULT 'N',
'just_trab_tst' char(1) DEFAULT 'N',
'just_trab_csjt' TEXT  DEFAULT 'N' ,
'stf' char(1) DEFAULT 'N',
'stj' char(1) DEFAULT 'N',
'cjf' char(1) DEFAULT 'N',
'cnj' char(1) DEFAULT 'N',
'just_mil_uniao_1grau' char(1) DEFAULT 'N',
'just_mil_uniao_stm' char(1) DEFAULT 'N',
'just_mil_est_1grau' char(1) DEFAULT 'N',
'just_mil_est_tjm' char(1) DEFAULT 'N',
'just_elei_1grau' char(1) DEFAULT 'N',
'just_elei_2grau' char(1) DEFAULT 'N',
'just_elei_tse' char(1) DEFAULT 'N',
'tipo_item' char(1) NOT NULL DEFAULT 'M',
'usu_inclusao' TEXT DEFAULT NULL,
'dat_inclusao' datetime DEFAULT NULL,
'dsc_ip_usu_inclusao' TEXT DEFAULT NULL,
'usu_alteracao' TEXT DEFAULT NULL,
PRIMARY KEY ('cod_movimento'),
FOREIGN KEY ('cod_movimento', 'tipo_item') REFERENCES 'itens' ('cod_item', 'tipo_item') ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE 'tipo_complemento' (
'seq_tipo_complemento' INTEGER NOT NULL ,
'desc_tipo_complemento' TEXT NOT NULL,
'dsc_observacao' text,
PRIMARY KEY ('seq_tipo_complemento')
);
CREATE TABLE 'complemento' (
'seq_complemento' INTEGER NOT NULL ,
'seq_tipo_complemento' INTEGER NOT NULL,
'dsc_complemento' TEXT NOT NULL,
'dsc_observacao' text,
PRIMARY KEY ('seq_complemento'),
FOREIGN KEY ('seq_tipo_complemento') REFERENCES 'tipo_complemento' ('seq_tipo_complemento') ON DELETE NO ACTION ON UPDATE NO ACTION
);
CREATE TABLE 'complemento_movimento' (
'seq_compl_mov' INTEGER NOT NULL ,
'seq_complemento' INTEGER NOT NULL,
'cod_movimento' INTEGER NOT NULL,
'data_inclusao' datetime NOT NULL,
'usu_inclusao' TEXT DEFAULT NULL,
PRIMARY KEY ('seq_compl_mov'),
FOREIGN KEY ('cod_movimento') REFERENCES 'movimentos' ('cod_movimento') ON DELETE NO ACTION ON UPDATE NO ACTION,
FOREIGN KEY ('seq_complemento') REFERENCES 'complemento' ('seq_complemento') ON DELETE NO ACTION ON UPDATE NO ACTION
);
CREATE TABLE 'complemento_tabelado' (
'seq_compl_tabelado' INTEGER NOT NULL ,
'seq_complemento' INTEGER NOT NULL,
'dsc_valor_tabelado' TEXT NOT NULL,
PRIMARY KEY ('seq_compl_tabelado'),
FOREIGN KEY ('seq_complemento') REFERENCES 'complemento' ('seq_complemento') ON DELETE NO ACTION ON UPDATE NO ACTION
);
CREATE TABLE 'procedimento_complementos' (
'id' INTEGER NOT NULL ,
'cod_movimento' INTEGER NOT NULL,
'seq_tipo_complemento' INTEGER NOT NULL,
'valor' TEXT NOT NULL,
'dat_inclusao' datetime NOT NULL,
'usu_inclusao' TEXT NOT NULL,
PRIMARY KEY ('id'),
FOREIGN KEY ('cod_movimento') REFERENCES 'movimentos' ('cod_movimento') ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE 'temporariedade' (
'seq_temp' INTEGER NOT NULL ,
'temporariedade' TEXT NOT NULL,
'txt_temp' TEXT NOT NULL,
'tipo_justica' char(1) NOT NULL,
'txt_tipo_justica' TEXT NOT NULL,
'ordem' INTEGER NOT NULL,
'status' char(1) NOT NULL,
PRIMARY KEY ('seq_temp')
);
CREATE TABLE 'tipo_ramo_justica' (
'seq_tipo_ramo_justica' INTEGER NOT NULL ,
'dsc_ramo_justica' TEXT DEFAULT NULL ,
'nom_ramo_justica' TEXT DEFAULT NULL ,
PRIMARY KEY ('seq_tipo_ramo_justica')
);
CREATE TABLE 'temp_item' (
'seq_temp_item' INTEGER NOT NULL  ,
'seq_item' INTEGER NOT NULL ,
'seq_temp' INTEGER NOT NULL ,
'tipo_item' TEXT NOT NULL ,
'temp_observacao' text ,
'seq_tipo_ramo_justica' INTEGER DEFAULT NULL ,
'usu_inclusao' TEXT NOT NULL ,
'dat_inclusao' datetime NOT NULL ,
PRIMARY KEY ('seq_temp_item'),
FOREIGN KEY ('seq_item', 'tipo_item') REFERENCES 'itens' ('cod_item', 'tipo_item') ON DELETE NO ACTION ON UPDATE NO ACTION,
FOREIGN KEY ('seq_temp') REFERENCES 'temporariedade' ('seq_temp') ON DELETE NO ACTION ON UPDATE NO ACTION,
FOREIGN KEY ('seq_tipo_ramo_justica') REFERENCES 'tipo_ramo_justica' ('seq_tipo_ramo_justica') ON DELETE NO ACTION ON UPDATE NO ACTION
);



CREATE INDEX '_cod_item' ON 'itens' ('cod_item');
CREATE INDEX '_cod_item_pai' ON 'itens' ('cod_item_pai');
CREATE INDEX '_cod_classe' ON 'classes' ('cod_classe');
CREATE INDEX '_cod_assunto' ON 'assuntos' ('cod_assunto');
CREATE INDEX '_cod_movimento' ON 'movimentos' ('cod_movimento');
CREATE INDEX '_FK_complemento' ON 'complemento' ('seq_tipo_complemento');
CREATE INDEX '_FK_complemento_movimento' ON 'complemento_movimento' ('seq_complemento');
CREATE INDEX '_FK2_complemento_movimento' ON 'complemento_movimento' ('cod_movimento');
CREATE INDEX '_FK_complemento_tabelado' ON 'complemento_tabelado' ('seq_complemento');
CREATE INDEX '_seq_item' ON 'procedimento_complementos' ('cod_movimento');
CREATE INDEX '_seq_tipo_complemento' ON 'procedimento_complementos' ('seq_tipo_complemento');
CREATE UNIQUE INDEX '_uk_teit_tipo_item' ON 'temp_item' ('seq_item','tipo_item','seq_tipo_ramo_justica');
CREATE INDEX '_fk_tipo_ramo_justica_teit' ON 'temp_item' ('seq_tipo_ramo_justica');
CREATE INDEX '_fk_temporalidade_teit' ON 'temp_item' ('seq_temp');
CREATE INDEX '_fk_itens_teit' ON 'temp_item' ('seq_item','tipo_item');

COMMIT;
PRAGMA ignore_check_constraints = ON;
PRAGMA foreign_keys = ON;
PRAGMA journal_mode = WAL;
PRAGMA synchronous = NORMAL;
