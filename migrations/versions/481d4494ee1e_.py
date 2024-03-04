"""empty message

Revision ID: 481d4494ee1e
Revises: 8e2e3a55e3c6
Create Date: 2024-03-04 19:12:32.738324

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '481d4494ee1e'
down_revision = '8e2e3a55e3c6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('hair_color', sa.String(length=250), nullable=True),
    sa.Column('gender', sa.String(length=250), nullable=True),
    sa.Column('birth_year', sa.String(length=250), nullable=False),
    sa.Column('mass', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('climate', sa.String(length=250), nullable=False),
    sa.Column('population', sa.String(length=250), nullable=False),
    sa.Column('diameter', sa.String(length=250), nullable=False),
    sa.Column('rotation_period', sa.String(length=250), nullable=False),
    sa.Column('orbital_period', sa.String(length=250), nullable=False),
    sa.Column('terrain', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('starship',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('model', sa.String(length=250), nullable=False),
    sa.Column('passengers', sa.String(length=250), nullable=False),
    sa.Column('length', sa.String(length=50), nullable=False),
    sa.Column('max_atmosphering_speed', sa.String(length=250), nullable=False),
    sa.Column('cargo_capacity', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorite',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('favoriteStarshipId', sa.Integer(), nullable=True),
    sa.Column('favoritePersonId', sa.Integer(), nullable=True),
    sa.Column('favoritePlanetId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['favoritePersonId'], ['people.id'], ),
    sa.ForeignKeyConstraint(['favoritePlanetId'], ['planets.id'], ),
    sa.ForeignKeyConstraint(['favoriteStarshipId'], ['starship.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('person')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.String(length=250), nullable=False))
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=80),
               type_=sa.String(length=250),
               existing_nullable=False)
        batch_op.create_unique_constraint(None, ['username'])
        batch_op.drop_column('is_active')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='unique')
        batch_op.alter_column('password',
               existing_type=sa.String(length=250),
               type_=sa.VARCHAR(length=80),
               existing_nullable=False)
        batch_op.drop_column('username')

    op.create_table('person',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('last_name', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='person_pkey'),
    sa.UniqueConstraint('name', name='person_name_key')
    )
    op.drop_table('favorite')
    op.drop_table('starship')
    op.drop_table('planets')
    op.drop_table('people')
    # ### end Alembic commands ###
