using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using static UnityEditor.Progress;
using TMPro;
using System;
using UnityEngine.iOS;
using Random = UnityEngine.Random;

public class Inventory : MonoBehaviour
{
   
    public static Inventory Singleton;
    public static InventoryItem carriedItem;

    [SerializeField] InventorySlot[] inventorySlots;
    [SerializeField] InventorySlot[] hotbarSlots;

    // 0=Head, 1=Chest, 2=Legs, 3=Feet
    [SerializeField] InventorySlot[] equipmentSlots;

    [SerializeField] RectTransform inventoryUI;
    [SerializeField] InventoryItem itemPrefab;

    [Header("Item List")]
    [SerializeField] Item[] items;

    [Header("Debug")]
    [SerializeField] Button giveItemBtn;

    [Header("Debug")]
    [SerializeField] Button clearItemBtn;
    public int itemcount { get; set; }
    public TextMeshProUGUI itemcountText { get; set; }
void Awake()
    {
        Singleton = this;
        giveItemBtn.onClick.AddListener(delegate { AddItemToInventory(PickRandomItem(), Random.Range(1, 10)) ; });
        clearItemBtn.onClick.AddListener(delegate { ClearSlot(inventorySlots[0]); }) ;

    }

    void Update()
    {
        if (carriedItem == null) return;

        carriedItem.transform.position = Input.mousePosition;
    }
   
    public void EquipEquipment(SlotTag tag, InventoryItem item = null)
    {
        switch (tag)
        {
            case SlotTag.Head:
                if (item == null)
                {
                    // Destroy item.equipmentPrefab on the Player Object;
                    Debug.Log("Unequipped helmet on " + tag);
                }
                else
                {
                    // Instantiate item.equipmentPrefab on the Player Object;
                    Debug.Log("Equipped " + item.myItem.name + " on " + tag);
                }
                break;
            case SlotTag.Chest:
                break;
            case SlotTag.Legs:
                break;
            case SlotTag.Feet:
                break;
        }
    }

    //en cours
    public void AddItemToInventory(Item itemToAdd, int quantity)
    {
        // Premi�re boucle : v�rifier si un item du m�me type est d�j� pr�sent et peut �tre stack�
        foreach (InventorySlot slot in inventorySlots)
        {
            if (slot.myItem != null)
            {
                if (AddToSlot(itemToAdd, quantity, slot))
                {
                    // Si l'item a �t� ajout� � un slot existant, on termine
                    return;
                }
                AddMax(itemToAdd, quantity, slot);
            }
            
        }

        // Deuxi�me boucle : v�rifier si un slot est vide pour ajouter l'item
        foreach (InventorySlot slot in inventorySlots)
        {
            if (AddToNewSlot(itemToAdd, quantity, slot))
            {
                // Si l'item a �t� ajout� dans un slot vide, on termine
                return;
            }
        }

        // Si l'item d�passe la capacit� maximale du stack, on ajuste les quantit�s
        foreach (InventorySlot slot in inventorySlots)
        {
            AddMax(itemToAdd, quantity, slot);
        }

    }


    public bool AddToNewSlot(Item itemToAdd, int quantity, InventorySlot slot)
    {
        if (slot.myItem == null && quantity <= itemToAdd.maxStack)
        {
            
            // Cr�e une nouvelle instance d'InventoryItem dans le slot
            InventoryItem newItem = Instantiate(itemPrefab, slot.transform);

            // Initialise l'item avec les infos de l'item � ajouter
            newItem.Initialize(itemToAdd, slot);

            // Met � jour la quantit�
            newItem.itemcount = quantity;

            // Mets � jour le texte de la quantit� dans le slotZ
            slot.itemcount = newItem.itemcount;
            slot.itemcountText.text = newItem.itemcount.ToString();

            // Assigne l'item au slot
            slot.myItem = newItem;
            
            
            return true ;
        }
        return false;
    }

    public bool AddToSlot(Item itemToAdd, int quantity, InventorySlot slot)
    {
        
        if (slot.myItem.ID == itemToAdd.ID && (quantity + slot.itemcount) <= itemToAdd.maxStack)
        {
            
            slot.itemcount += quantity;
            slot.itemcountText.text = slot.itemcount.ToString();
            print("oui");
            
            return true;
        }
        return false;
    }

    public void AddMax(Item itemToAdd, int quantity, InventorySlot slot)
    {
        if (slot.myItem.ID == itemToAdd.ID && (quantity + slot.itemcount) > itemToAdd.maxStack)
        {
            
            int remainingQuantity = quantity - (itemToAdd.maxStack - slot.itemcount);
            slot.itemcount = itemToAdd.maxStack;
            slot.itemcountText.text = slot.itemcount.ToString();

        }
    }

    

    public void ClearSlot(InventorySlot slot)
    {
        Destroy(slot.myItem.gameObject);  // D�truit l'image ou le prefab visuel de l'item
        slot.myItem = null;
        slot.itemcountText.text = string.Empty;
        slot.itemcount = 0;
    }
    public void SwapItem( InventorySlot slot1, InventorySlot slot2)
    {
        InventoryItem item_a = slot1.myItem;
        InventoryItem item_b = slot2.myItem;


        int count1 = slot1.itemcount;
        int count2 = slot2.itemcount;
        


        ClearSlot(slot1);
        
        ClearSlot(slot2);
        
        
        AddToNewSlot(item_a.myItem, count1, slot2);
        AddToNewSlot(item_b.myItem, count2, slot1);
    }
    Item PickRandomItem()
    {
        int random = Random.Range(0, items.Length);
        return items[random];
    }
}