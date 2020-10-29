"""empty message

Revision ID: 9a17287ebd83
Revises: 
Create Date: 2020-09-28 15:33:26.693095

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a17287ebd83'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('nodes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('bokes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('content', sa.String(length=2000), nullable=True),
    sa.Column('created_time', sa.Integer(), nullable=True),
    sa.Column('see_num', sa.Integer(), nullable=True),
    sa.Column('star_num', sa.Integer(), nullable=True),
    sa.Column('thumbs', sa.Integer(), nullable=True),
    sa.Column('node_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['node_id'], ['nodes.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=100), nullable=True),
    sa.Column('created_time', sa.Integer(), nullable=True),
    sa.Column('thumbs', sa.Integer(), nullable=True),
    sa.Column('boke_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['boke_id'], ['bokes.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sees',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('boke_id', sa.Integer(), nullable=True),
    sa.Column('ip', sa.String(length=32), nullable=True),
    sa.Column('created_time', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['boke_id'], ['bokes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stars',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('boke_id', sa.Integer(), nullable=True),
    sa.Column('flag', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['boke_id'], ['bokes.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('boke_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['boke_id'], ['bokes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('replys',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=100), nullable=True),
    sa.Column('created_time', sa.Integer(), nullable=True),
    sa.Column('thumbs', sa.Integer(), nullable=True),
    sa.Column('reply_id', sa.Integer(), nullable=True),
    sa.Column('comment_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['comment_id'], ['comments.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('replys')
    op.drop_table('tags')
    op.drop_table('stars')
    op.drop_table('sees')
    op.drop_table('comments')
    op.drop_table('bokes')
    op.drop_table('users')
    op.drop_table('nodes')
    # ### end Alembic commands ###
