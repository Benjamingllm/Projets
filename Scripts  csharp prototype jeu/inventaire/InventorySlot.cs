using System.Collections;
using System.Collections.Generic;
using TMPro;
using Unity.VisualScripting;
using UnityEngine;
using UnityEngine.EventSystems;

public enum SlotTag { None, Head, Chest, Legs, Feet }

public class InventorySlot : MonoBehaviour, IDropHandler
{
    public InventoryItem myItem;
    public int itemcount = 0;
    public TextMeshProUGUI itemcountText;
    
    public SlotTag myTag;

    public void Awake()
    {

            this.itemcountText.text = string.Empty;
        
    }


    public void SetItem(InventoryItem item)
    {
        Inventory.carriedItem = null;

        // Reset old slot
        item.activeSlot.myItem = null;

        // Set current slot
        myItem = item;
        myItem.activeSlot = this;
        myItem.transform.SetParent(transform);
        myItem.canvasGroup.blocksRaycasts = true;

        if (myTag != SlotTag.None)
        { Inventory.Singleton.EquipEquipment(myTag, myItem); }
    }

    void IDropHandler.OnDrop(PointerEventData eventData)
    {
        GameObject dropped = eventData.pointerDrag;
        InventoryItem draggableItem = dropped.GetComponent<InventoryItem>();

        if(this.myItem == null) 
        {
            Inventory.Singleton.AddToNewSlot(draggableItem.myItem, draggableItem.activeSlot.itemcount, this);
            Inventory.Singleton.ClearSlot(draggableItem.activeSlot);
            return;
        }

        if (this.myItem != null )
        {
            Inventory.Singleton.SwapItem(draggableItem.activeSlot, this) ;
            return;
            
        }
        
        
    }

    
}