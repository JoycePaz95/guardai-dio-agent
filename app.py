import sqlite3

def autenticar_usuario(usuario, senha):
    conexao = sqlite3.connect("guardai_users.db")
    cursor = conexao.cursor()
    
    # Consulta segura: uso de placeholders (Prepared Statement)
    consulta = "SELECT id, username, role FROM users WHERE username = ? AND password = ?"
    cursor.execute(consulta, (usuario, senha))
    
    resultado = cursor.fetchone()
    conexao.close()
    return resultado

if __name__ == "__main__":
    print(autenticar_usuario("admin", "1234"))
