#!/usr/bin/env python3
"""
Skill Hub CLI: Busca, visualização e instalação de skills sob demanda para projetos.
"""
import sys
import os
import json
import shutil
import argparse
from pathlib import Path
import urllib.request
import urllib.error

HUB_DIR = Path(__file__).resolve().parent.parent
INDEX_FILE = HUB_DIR / "catalog" / "skills_index.json"
CACHE_DIR = Path.home() / ".cache" / "agentic-awesome-skills"
CORE_SKILLS_DIR = HUB_DIR / "skills"
GITHUB_RAW_BASE = "https://raw.githubusercontent.com/sickn33/agentic-awesome-skills/main"

def load_index():
    if not INDEX_FILE.exists():
        print(f"Erro: Arquivo de índice não encontrado em {INDEX_FILE}", file=sys.stderr)
        sys.exit(1)
    with open(INDEX_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def search_skills(query, limit=10):
    skills = load_index()
    q = query.lower()
    results = []
    
    for item in skills:
        s_id = item.get("id", "").lower()
        s_name = item.get("name", "").lower()
        s_cat = item.get("category", "").lower()
        s_desc = item.get("description", "").lower()
        
        score = 0
        if q == s_id or q == s_name:
            score += 100
        elif q in s_id or q in s_name:
            score += 50
        elif q in s_cat:
            score += 20
        elif q in s_desc:
            score += 10
            
        if score > 0:
            results.append((score, item))
            
    results.sort(key=lambda x: x[0], reverse=True)
    return [r[1] for r in results[:limit]]

def cmd_search(args):
    results = search_skills(args.query, limit=args.limit)
    if not results:
        print(f"Nenhuma skill encontrada para o termo: '{args.query}'")
        return
    print(f"Encontradas {len(results)} skills correspondentes a '{args.query}':\n")
    for s in results:
        s_id = s.get("id")
        cat = s.get("category", "geral")
        desc = s.get("description", "").strip()
        if len(desc) > 120:
            desc = desc[:117] + "..."
        print(f"• \033[1m{s_id}\033[0m [{cat}]")
        print(f"  {desc}\n")

def cmd_info(args):
    skills = load_index()
    skill_id = args.skill_id
    found = next((s for s in skills if s.get("id") == skill_id), None)
    if not found:
        print(f"Skill '{skill_id}' não encontrada no catálogo.", file=sys.stderr)
        return
        
    print("=" * 60)
    print(f"Skill ID: {found.get('id')}")
    print(f"Nome:     {found.get('name')}")
    print(f"Categoria:{found.get('category')}")
    print(f"Origem:   {found.get('source')}")
    print(f"Descrição:\n{found.get('description')}")
    print("=" * 60)
    
    # Exibir preview do SKILL.md se disponível no cache
    cached_path = CACHE_DIR / "skills" / skill_id / "SKILL.md"
    if cached_path.exists():
        print("\n--- Preview do SKILL.md (primeiras 25 linhas) ---")
        with open(cached_path, "r", encoding="utf-8") as f:
            for i, line in enumerate(f):
                if i >= 25:
                    print("...")
                    break
                print(line, end="")

def cmd_install(args):
    skill_id = args.skill_id
    target_dir = Path(args.target_path).resolve()
    
    if not target_dir.exists():
        print(f"Erro: O diretório de destino não existe: {target_dir}", file=sys.stderr)
        sys.exit(1)
        
    # Destino padrão: .agents/skills/<skill_id>
    dest_skills_dir = target_dir / ".agents" / "skills" / skill_id
    
    # 1. Tentar instalar do cache local
    src_cached = CACHE_DIR / "skills" / skill_id
    if src_cached.exists() and src_cached.is_dir():
        dest_skills_dir.parent.mkdir(parents=True, exist_ok=True)
        if dest_skills_dir.exists():
            shutil.rmtree(dest_skills_dir)
        shutil.copytree(src_cached, dest_skills_dir)
        print(f"✓ Skill '{skill_id}' instalada com sucesso em:")
        print(f"  {dest_skills_dir}")
        return
        
    # 2. Se não estiver no cache local, tentar baixar via GitHub raw
    print(f"Skill '{skill_id}' não encontrada no cache local. Tentando baixar do GitHub...")
    skill_url = f"{GITHUB_RAW_BASE}/skills/{skill_id}/SKILL.md"
    try:
        req = urllib.request.Request(skill_url, headers={"User-Agent": "SkillHub/1.0"})
        with urllib.request.urlopen(req) as response:
            content = response.read().decode("utf-8")
            dest_skills_dir.mkdir(parents=True, exist_ok=True)
            with open(dest_skills_dir / "SKILL.md", "w", encoding="utf-8") as out:
                out.write(content)
            print(f"✓ SKILL.md de '{skill_id}' baixado e instalado com sucesso em:")
            print(f"  {dest_skills_dir / 'SKILL.md'}")
    except Exception as e:
        print(f"Falha ao obter skill '{skill_id}': {e}", file=sys.stderr)
        sys.exit(1)

def cmd_list_core(args):
    print("Skills Core do Hub Central (instaladas localmente):\n")
    if CORE_SKILLS_DIR.exists():
        for item in sorted(CORE_SKILLS_DIR.iterdir()):
            if item.is_dir() and (item / "SKILL.md").exists():
                print(f"• {item.name}")

def main():
    parser = argparse.ArgumentParser(description="Skill Hub CLI - Gerenciador de Skills para Agentes")
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    # search
    p_search = subparsers.add_parser("search", help="Pesquisar skills no catálogo")
    p_search.add_argument("query", help="Termo de pesquisa (ex: react, docker, tailwind)")
    p_search.add_argument("--limit", type=int, default=10, help="Número máximo de resultados")
    p_search.set_defaults(func=cmd_search)
    
    # info
    p_info = subparsers.add_parser("info", help="Ver detalhes de uma skill")
    p_info.add_argument("skill_id", help="ID da skill (ex: react-best-practices)")
    p_info.set_defaults(func=cmd_info)
    
    # install
    p_install = subparsers.add_parser("install", help="Instalar uma skill em um projeto alvo")
    p_install.add_argument("skill_id", help="ID da skill a instalar")
    p_install.add_argument("target_path", help="Caminho do repositório/projeto alvo")
    p_install.set_defaults(func=cmd_install)
    
    # list-core
    p_list = subparsers.add_parser("list-core", help="Listar skills core do Hub Central")
    p_list.set_defaults(func=cmd_list_core)
    
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
