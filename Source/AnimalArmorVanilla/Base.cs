namespace AnimalArmorVanilla
{
    class Base : ModBase
    {
        public override string ModIdentifier => "AnimalArmorVanilla";
        public static Base Instance { get; private set; }
        // private ExtendedDataStorage _extendedDataStorage;

        public Base()
        {
            Instance = this;
        }
        // public ExtendedDataStorage GetExtendedDataStorage()
        // {
        //     return _extendedDataStorage;
        // }
        // public override void WorldLoaded()
        // {
        //     _extendedDataStorage = UtilityWorldObjectManager.GetUtilityWorldObject<ExtendedDataStorage>();
        //     base.WorldLoaded();
        // }
    }


}
