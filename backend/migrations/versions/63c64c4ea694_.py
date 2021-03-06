"""empty message

Revision ID: 63c64c4ea694
Revises: 
Create Date: 2021-05-03 22:57:00.276639

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '63c64c4ea694'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('character',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('image', sa.String(length=200), nullable=False),
    sa.Column('age', sa.String(length=100), nullable=False),
    sa.Column('job', sa.String(length=50), nullable=False),
    sa.Column('quote', sa.Text(), nullable=False),
    sa.Column('word_cloud', sa.String(length=200), nullable=False),
    sa.Column('youtube', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('overdose',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question_number', sa.Integer(), nullable=False),
    sa.Column('question', sa.Text(), nullable=False),
    sa.Column('answer', sa.String(length=100), nullable=False),
    sa.Column('select_1', sa.String(length=100), nullable=False),
    sa.Column('select_2', sa.String(length=100), nullable=False),
    sa.Column('select_3', sa.String(length=100), nullable=False),
    sa.Column('select_4', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('overdose_result',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rank', sa.Integer(), nullable=False),
    sa.Column('image', sa.String(length=200), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('survey',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question_number', sa.Integer(), nullable=False),
    sa.Column('question', sa.Text(), nullable=False),
    sa.Column('image', sa.String(length=200), nullable=False),
    sa.Column('select_1', sa.String(length=200), nullable=False),
    sa.Column('select_2', sa.String(length=200), nullable=False),
    sa.Column('select_3', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('survey_result',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image', sa.Text(), nullable=False),
    sa.Column('nick_name', sa.String(length=100), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('pair', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('word',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('emotion', sa.String(length=50), nullable=False),
    sa.Column('word', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('connection',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('target', sa.Integer(), nullable=False),
    sa.Column('source', sa.Integer(), nullable=False),
    sa.Column('origin_type', sa.String(length=50), nullable=True),
    sa.Column('connection_weight', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['source'], ['character.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['target'], ['character.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('emotion',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('joy', sa.Integer(), nullable=False),
    sa.Column('anger', sa.Integer(), nullable=False),
    sa.Column('sadness', sa.Integer(), nullable=False),
    sa.Column('character_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['character_id'], ['character.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('gacha',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('gacha_number', sa.Integer(), nullable=False),
    sa.Column('nickname', sa.Text(), nullable=False),
    sa.Column('quote', sa.Text(), nullable=False),
    sa.Column('question', sa.Text(), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('character_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['character_id'], ['character.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stock',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('episode', sa.Integer(), nullable=False),
    sa.Column('weight', sa.Integer(), nullable=False),
    sa.Column('character_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['character_id'], ['character.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stock')
    op.drop_table('gacha')
    op.drop_table('emotion')
    op.drop_table('connection')
    op.drop_table('word')
    op.drop_table('survey_result')
    op.drop_table('survey')
    op.drop_table('overdose_result')
    op.drop_table('overdose')
    op.drop_table('character')
    # ### end Alembic commands ###
