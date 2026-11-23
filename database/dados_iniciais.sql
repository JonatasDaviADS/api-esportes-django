-- =========================================================
-- API Loja de Esportes - Dados iniciais (seed)
-- ORDEM DE USO:
--   1) Criar o banco (comando abaixo) no phpMyAdmin
--   2) Rodar "python manage.py migrate" (cria a tabela)
--   3) Voltar ao phpMyAdmin e rodar o INSERT deste arquivo
-- =========================================================

CREATE DATABASE IF NOT EXISTS loja_esportes CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE loja_esportes;   -- "entra" no banco antes do INSERT

INSERT INTO artigos_esportivos (nome, marca, modelo, cor, valor, ano, modalidade) VALUES
('Chuteira Predator', 'Adidas', 'Elite FG', 'Preta', 899.90, 2025, 'Futebol'),
('Chuteira Mercurial', 'Nike', 'Superfly 10', 'Rosa', 1299.90, 2025, 'Futebol'),
('Bola de Futebol', 'Adidas', 'Al Rihla Pro', 'Branca', 499.90, 2022, 'Futebol'),
('Camisa de Time', 'Puma', 'Home 2025', 'Azul', 349.90, 2025, 'Futebol'),
('Tênis de Corrida', 'Nike', 'Pegasus 41', 'Preta', 799.90, 2024, 'Corrida'),
('Tênis de Corrida', 'Asics', 'Gel-Nimbus 26', 'Azul', 999.90, 2024, 'Corrida'),
('Relógio GPS', 'Garmin', 'Forerunner 265', 'Preta', 2499.90, 2023, 'Corrida'),
('Bola de Basquete', 'Wilson', 'Evolution', 'Laranja', 459.90, 2023, 'Basquete'),
('Tênis de Basquete', 'Nike', 'LeBron 22', 'Branca', 1199.90, 2025, 'Basquete'),
('Raquete de Tênis', 'Wilson', 'Pro Staff 97', 'Preta', 1599.90, 2024, 'Tênis'),
('Bola de Tênis', 'Head', 'Championship', 'Amarela', 39.90, 2023, 'Tênis'),
('Bola de Vôlei', 'Mikasa', 'V200W', 'Amarela', 599.90, 2022, 'Vôlei'),
('Joelheira', 'Asics', 'Gel Kneepad', 'Preta', 189.90, 2024, 'Vôlei'),
('Óculos de Natação', 'Speedo', 'Fastskin Pure', 'Azul', 249.90, 2025, 'Natação'),
('Capacete de Ciclismo', 'Specialized', 'Prevail 3', 'Branca', 1899.90, 2025, 'Ciclismo');