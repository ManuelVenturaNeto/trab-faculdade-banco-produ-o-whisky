# src/infra/config/populate_db.py
from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities import *
from datetime import datetime, timedelta
import random

def populate_database():
    print("Populating database with comprehensive sample data...")
    db_handler = DBConnectionHandler()
    
    with db_handler.get_db() as db:
        try:
            # Clear existing data
            db.query(Empacotamentos).delete()
            db.query(Maturacoes).delete()
            db.query(Destilacoes).delete()
            db.query(Fermentacoes).delete()
            db.query(Mosturacoes).delete()
            db.query(LoteIngredientes).delete()
            db.query(Ingredientes).delete()
            db.query(Tanques).delete()
            db.query(Phs).delete()
            db.query(Temperaturas).delete()
            db.query(TeorAlcoolicos).delete()
            db.query(Vazoes).delete()
            db.query(Densidades).delete()
            db.commit()
            print("Database cleared successfully!")
            
            # ===== CREATE INGREDIENTS =====
            ingredients = [
                Ingredientes(nome="Malte de Cevada Pilsen", tipo="Cevada", fornecedor="Maltaria A", validade=datetime.now() + timedelta(days=365)),
                Ingredientes(nome="Malte de Trigo", tipo="Trigo", fornecedor="Maltaria B", validade=datetime.now() + timedelta(days=300)),
                Ingredientes(nome="Malte de Centeio", tipo="Centio", fornecedor="Maltaria C", validade=datetime.now() + timedelta(days=330)),
                Ingredientes(nome="Malte Caramelo", tipo="Cevada", fornecedor="Maltaria D", validade=datetime.now() + timedelta(days=280)),
                Ingredientes(nome="Malte Defumado", tipo="Cevada", fornecedor="Maltaria E", validade=datetime.now() + timedelta(days=320)),
                Ingredientes(nome="Água Mineral", tipo="Água", fornecedor="Fonte Natural", validade=datetime.now() + timedelta(days=180)),
                Ingredientes(nome="Lúpulo Cascade", tipo="Lúpulo", fornecedor="Hop Farm", validade=datetime.now() + timedelta(days=200)),
                Ingredientes(nome="Lúpulo Saaz", tipo="Lúpulo", fornecedor="Hop Farm", validade=datetime.now() + timedelta(days=210)),
                Ingredientes(nome="Levedura US-05", tipo="Levedura", fornecedor="Fermentis", validade=datetime.now() + timedelta(days=150)),
                Ingredientes(nome="Levedura Scottish Ale", tipo="Levedura", fornecedor="Fermentis", validade=datetime.now() + timedelta(days=160))
            ]
            db.add_all(ingredients)
            db.commit()
            print(f"Created {len(ingredients)} ingredients")
            
            # ===== CREATE TANKS =====
            tanks = [
                Tanques(nome="MT-01", tipo="Mosturação", capacidade=5000, status_tanque="Disponível", descricao="Tanque de mostura em aço inox"),
                Tanques(nome="MT-02", tipo="Mosturação", capacidade=4000, status_tanque="Em manutenção", descricao="Tanque de mostura com agitador"),
                Tanques(nome="FT-01", tipo="Fermentação", capacidade=8000, status_tanque="Disponível", descricao="Tanque com controle de temperatura"),
                Tanques(nome="FT-02", tipo="Fermentação", capacidade=10000, status_tanque="Ocupado", descricao="Tanque de fermentação principal"),
                Tanques(nome="DT-01", tipo="Destilação", capacidade=3000, status_tanque="Disponível", descricao="Alambique de cobre"),
                Tanques(nome="DT-02", tipo="Destilação", capacidade=3500, status_tanque="Ocupado", descricao="Coluna de destilação"),
                Tanques(nome="AT-01", tipo="Armazenamento", capacidade=15000, status_tanque="Ocupado", descricao="Barril de carvalho #1"),
                Tanques(nome="AT-02", tipo="Armazenamento", capacidade=15000, status_tanque="Ocupado", descricao="Barril de carvalho #2"),
                Tanques(nome="AT-03", tipo="Armazenamento", capacidade=15000, status_tanque="Disponível", descricao="Barril de carvalho #3"),
                Tanques(nome="BT-01", tipo="Bottling", capacidade=2000, status_tanque="Disponível", descricao="Tanque de envase")
            ]
            db.add_all(tanks)
            db.commit()
            print(f"Created {len(tanks)} tanks")
            
            # ===== CREATE INGREDIENT LOTS =====
            lots = []
            for i in range(1, 11):
                lot = LoteIngredientes(
                    ingrediente_id=random.randint(1, 10),
                    quantidade=random.randint(500, 2000),
                    unidade="kg",
                    data_recebimento=datetime.now() - timedelta(days=random.randint(1, 60))
                )
                lots.append(lot)
            db.add_all(lots)
            db.commit()
            print(f"Created {len(lots)} ingredient lots")
            
            # ===== CREATE MEASUREMENTS =====
            # pH Measurements
            phs = []
            for _ in range(15):
                ph = Phs(
                    valor=random.uniform(5.0, 7.0),
                    momento_leitura=datetime.now() - timedelta(hours=random.randint(1, 240))
                )
                phs.append(ph)
            db.add_all(phs)
            db.commit()
            print(f"Created {len(phs)} pH measurements")
            
            # Temperature Measurements
            temps = []
            for _ in range(15):
                temp = Temperaturas(
                    valor=random.randint(15, 100),
                    momento_leitura=datetime.now() - timedelta(hours=random.randint(1, 240))
                )
                temps.append(temp)
            db.add_all(temps)
            db.commit()
            print(f"Created {len(temps)} temperature measurements")
            
            # Density Measurements
            densities = []
            for _ in range(15):
                density = Densidades(
                    valor=random.uniform(1.000, 1.100),
                    momento_leitura=datetime.now() - timedelta(hours=random.randint(1, 240))
                )
                densities.append(density)
            db.add_all(densities)
            db.commit()
            print(f"Created {len(densities)} density measurements")
            
            # Alcohol Measurements
            alcohols = []
            for _ in range(15):
                alcohol = TeorAlcoolicos(
                    valor=random.uniform(40.0, 70.0),
                    momento_leitura=datetime.now() - timedelta(hours=random.randint(1, 240))
                )
                alcohols.append(alcohol)
            db.add_all(alcohols)
            db.commit()
            print(f"Created {len(alcohols)} alcohol measurements")
            
            # Flow Measurements
            flows = []
            for _ in range(15):
                flow = Vazoes(
                    valor=random.randint(50, 200),
                    momento_leitura=datetime.now() - timedelta(hours=random.randint(1, 240)),
                    tipo=random.choice(["Entrada", "Saída"])
                )
                flows.append(flow)
            db.add_all(flows)
            db.commit()
            print(f"Created {len(flows)} flow measurements")
            
            # ===== CREATE PRODUCTION PROCESSES =====
            # Mashing Processes
            mashings = []
            for i in range(1, 11):
                mashing = Mosturacoes(
                    ph_id=random.randint(1, 15),
                    temperatura_id=random.randint(1, 15),
                    lote_ingrediente_id=i,
                    tanque_id=random.choice([1, 2]),
                    inicio_processo=datetime.now() - timedelta(days=30-i),
                    fim_processo=datetime.now() - timedelta(days=29-i)
                )
                mashings.append(mashing)
            db.add_all(mashings)
            db.commit()
            print(f"Created {len(mashings)} mashing processes")
            
            # Fermentation Processes
            fermentations = []
            for i in range(1, 11):
                fermentation = Fermentacoes(
                    mosturacao_id=i,
                    ph_id=random.randint(16, 30) if i > 5 else random.randint(1, 15),  # Use different IDs
                    temperatura_id=random.randint(16, 30) if i > 5 else random.randint(1, 15),
                    densidade_id=random.randint(1, 15),
                    tanque_id=random.choice([3, 4]),
                    inicio_processo=datetime.now() - timedelta(days=29-i),
                    fim_processo=datetime.now() - timedelta(days=22-i)
                )
                fermentations.append(fermentation)
            db.add_all(fermentations)
            db.commit()
            print(f"Created {len(fermentations)} fermentation processes")
            
            # Distillation Processes
            distillations = []
            for i in range(1, 11):
                distillation = Destilacoes(
                    fermentacao_id=i,
                    tanque_id=random.choice([5, 6]),
                    vazao_id=random.randint(1, 15),
                    teor_alcoolico_id=random.randint(1, 15),
                    inicio_processo=datetime.now() - timedelta(days=22-i),
                    fim_processo=datetime.now() - timedelta(days=21-i)
                )
                distillations.append(distillation)
            db.add_all(distillations)
            db.commit()
            print(f"Created {len(distillations)} distillation processes")
            
            # Maturation Processes
            maturations = []
            for i in range(1, 11):
                maturation = Maturacoes(
                    destilacao_id=i,
                    inicio_processo=datetime.now() - timedelta(days=21-i),
                    fim_processo=datetime.now() - timedelta(days=random.randint(1, 10))
                )
                maturations.append(maturation)
            db.add_all(maturations)
            db.commit()
            print(f"Created {len(maturations)} maturation processes")
            
            # Packaging Processes
            packagings = []
            for i in range(1, 11):
                packaging = Empacotamentos(
                    maturacao_id=i,
                    data_empacotamento=datetime.now() - timedelta(days=random.randint(1, 5)),
                    tipo_garrafa=random.choice(["Vidro escuro 0.7L", "Vidro claro 0.5L", "Cerâmica 1L"]),
                    litros_garrafa=random.choice([0.5, 0.7, 1.0]),
                    lote=1000 + i
                )
                packagings.append(packaging)
            db.add_all(packagings)
            db.commit()
            print(f"Created {len(packagings)} packaging processes")
            
            print("\nDatabase populated successfully!")
            print("Total records created:")
            print(f"- Ingredients: {len(ingredients)}")
            print(f"- Tanks: {len(tanks)}")
            print(f"- Ingredient Lots: {len(lots)}")
            print(f"- pH Measurements: {len(phs)}")
            print(f"- Temperature Measurements: {len(temps)}")
            print(f"- Density Measurements: {len(densities)}")
            print(f"- Alcohol Measurements: {len(alcohols)}")
            print(f"- Flow Measurements: {len(flows)}")
            print(f"- Mashing Processes: {len(mashings)}")
            print(f"- Fermentation Processes: {len(fermentations)}")
            print(f"- Distillation Processes: {len(distillations)}")
            print(f"- Maturation Processes: {len(maturations)}")
            print(f"- Packaging Processes: {len(packagings)}")
            
            
        except Exception as e:
            db.rollback()
            print(f"Error populating database: {e}")
            raise