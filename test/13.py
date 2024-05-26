sword_phys, sword_magic = map(int, input().split())
bow_phys, spell_magic = map(int, input().split())
repel_phys, repel_magic = map(int, input().split())

max_sword = max(sword_magic - repel_magic, 0) + max(sword_phys - repel_phys, 0)

print(max(max_sword,
          max(bow_phys - repel_phys, 0),
          max(spell_magic - repel_magic, 0)))