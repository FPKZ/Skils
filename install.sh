#!/usr/bin/env bash
set -e

REPO_URL="https://github.com/SEU_USUARIO/skils.git"
INSTALL_DIR="$HOME/.local/share/antigravity-skills"

echo "=== Instalador do Hub Central de Skills para Antigravity ==="
echo "Instalando em: $INSTALL_DIR..."

# 1. Se já existir instalação anterior, atualiza; senão clona
if [ -d "$INSTALL_DIR/.git" ]; then
  echo "-> Atualizando instalação existente..."
  cd "$INSTALL_DIR" && git pull --quiet
else
  echo "-> Baixando o Hub de Skills..."
  mkdir -p "$(dirname "$INSTALL_DIR")"
  rm -rf "$INSTALL_DIR"
  git clone --depth 1 "$REPO_URL" "$INSTALL_DIR"
fi

# 2. Executa a configuração da máquina
cd "$INSTALL_DIR"
chmod +x setup.sh
./setup.sh

echo ""
echo "🎉 Pronto! Todas as skills e o Agente 0 foram instalados e ativados no seu Antigravity."
