import datetime
from sqlalchemy import*
from sqlalchemy.orm import declarative_base, ralationship, sessionmaker
DATABASE_URL="postgresql://postgres:1234@localhost:5432/postgres"
engine=create_engine(DATABASE_URL)
SessionLocal1=sessionmaker(autocommit=False, autoflush=False, blind=engine)
Base=declarative_base()

class Usuario(Base):
    __tablename__="usuario"
    id=Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome=Column(String(255), nullable=False)
    email=Column(String(255), nullable=False)
    senha_hash=Column(String(255), nullable=False)
    criado_em=Column(DateTime(timezone=True), default=datetime.datetime.now)

    notas= ralationship("Nota", back_populates="autor")
    usuario_endereços=ralationship("Enderecos",
        secondary=usuario_endereco_associacao,
        back_populates="moradores"
    )
    class nota(Base):
        __tablename__="notas"
        id=Column(Integer, primary_key=true, index=True, autoincrement=True)
        id_usuario=Column(Integer, ForeignKey("usuario.id"), nullable=False)
        titulo=Column(String(255), nullable=False)
        conteudo=Column(text)
        criado_em=Column(DateTime(timezone=True), default=datetime.datetime.now)
        modificado_em=Column(DateTime(timezone=True), default=datetime.datetime.now)
        autor=relationship("Usuario", back_populates="Notas")
